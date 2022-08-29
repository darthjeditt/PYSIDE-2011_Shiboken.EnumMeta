# -*- coding: utf-8 -*-
'''Threading utilities'''

from __future__ import annotations

import time
import threading
import proxi.common as common
import proxi.console as console
import proxi.debug as debug
from PySide6 import QtCore
from typing import Callable


class ThreadResultWrapper:
    '''Wrapper for sending a thread result back to caller via `QtCore.Signal`'''

    def __init__(self, sourceThread: EmittingThread, targetMethod: Callable, payload: object|None, callbacks: Callable|list[Callable]|None, error: Exception|None, resetBusyState: bool, teminateRequested: bool=False) -> None:
        '''Wrapper for sending a thread result back to caller via `QtCore.Signal`

        Args:
            sourceThread (EmittingThread): The source thread for this signal
            targetMethod (Callable): The target method that was executed on `sourceThread`
            payload (object): The result output from `targetMethod`
            callbacks (Callable): Callbacks, if any. Single or list. Will be sanitized during init
            error (Exception): Exception thrown by thread, if any
            resetBusyState (bool): Reset busy-state after completion?
            teminateRequested (bool, optional): Has thread termination been requested?. Defaults to False.
        '''

        self.sourceThread = sourceThread
        self.payload = payload
        self.targetMethod = targetMethod
        self.resetBusyState = resetBusyState
        self.error = error
        self.teminateRequested = teminateRequested
        self.die = teminateRequested

        self.callbacks: list[Callable]|None = None
        if self.teminateRequested:
            self.callbacks = None
        elif common.isIterable(callbacks):
            self.callbacks = callbacks # type: ignore
        elif callbacks:
            self.callbacks = [callbacks] # type: ignore


class EmittingThread(QtCore.QThread):
    '''Wrapper for QThread that emits a `ThreadResultWrapper` signal when completed'''

    finished = QtCore.Signal(ThreadResultWrapper)

    def __init__(self, target: Callable, targetPayload: object=None, callbacks: Callable|list[Callable]|None=None, resetBusyState: bool=True, parent: QtCore.QObject|None=None) -> None:
        '''Wrapper for QThread that emits a `ThreadResultWrapper` signal when completed

        To start the execution of this thread, `.start()` must explicitly be called. See `QtCore.QThread` docs for further details.

        Args:
            target (Callable): Target method to run during thread execution
            targetPayload (object, optional): Payload to send to `target` if applicable. Defaults to None.
            callbacks (Callable, optional): Callbacks to run at receiving end. Passthrough for this thread instance, to be actioned back on caller thread. Defaults to None.
            resetBusyState (bool, optional): Reset busy state when completed? Passthrough for this thread instance, to be actioned back on caller thread. Defaults to True.
            parent (QtCore.QObject, optional): Parent QObject. If none, Qt will automatically assume whatever is most convenient. Defaults to None.
        '''

        self.target = target
        self.targetPayload = targetPayload
        self.callbacks = callbacks
        self.resetBusyState = resetBusyState
        self._die = False
        super().__init__(parent=parent)

    def kill(self):
        '''Attempts to terminate the thread, and marks the resulting signal with a `do not execute` signal'''

        self._die = True
        self.terminate()

    @debug.timing
    def run(self):
        '''Thread execution, initiated by `start()`'''

        result = None
        error = None

        try:
            result = self.target(self.targetPayload) if self.targetPayload is not None else self.target()
        except Exception as e:
            console.error(f'Error encountered while executing method `{self.target}` on thread {self}')
            error = e

        if self._die:
            return

        self.finished.emit( # type: ignore
            ThreadResultWrapper(
                sourceThread=self,
                targetMethod = self.target,
                payload = result,
                callbacks = self.callbacks,
                error = error,
                resetBusyState = self.resetBusyState,
                teminateRequested=self._die
        ))


class SingleThread(threading.Thread):
    '''Generic thread for API calls, taking a target method and (optional) callback method reference'''

    def __init__(self, target: Callable, callbacks: Callable|list[Callable]=None) -> None:
        '''Generic thread for API calls, taking a target method and (optional) callback method reference.

        To start the execution of this thread, `.start()` must explicitly be called. See `threading.Thread` docs for further details.
        
        Args:
            target (Callable): Target method to execute
            callbacks (Callable|list[Callable], optional): Callback method(s) to execute after thread is finished. Must accept `targetReference, *args, **kwargs` payload -> the latter two being the result from `target()`
        '''

        self.target = target
        self.callbacks = callbacks
        self._die: bool = False
        super().__init__(target=self.wrapper)

    def kill(self):
        '''This does not exactly kill the thread, but will prevent them from executing callbacks'''

        self._die = True

    @debug.timing
    def wrapper(self) -> None:
        result = self.target()

        if self._die:
            return

        if self.callbacks:
            if not common.isIterable(self.callbacks):
                self.callbacks = [self.callbacks]

            callback: Callable
            for callback in self.callbacks: # type: ignore
                if self._die:
                    return

                callback(self.target, result)


class MultiThreadWrapper:
    '''Generic multi-thread call to an arbitrary number of target methods'''

    def __init__(self, targets: Callable|list[Callable], callbacks: Callable|list[Callable]|None=None) -> None:
        '''Generic multi-thread call to an arbitrary number of target methods.

        To start the execution of this thread, `.start()` must explicitly be called.

        Blocks until completed.

        Args:
            targets (Callable): Target methods to execute
            callbacks (Callable|list[Callable], optional): Callback method(s) to execute after thread is finished. Must accept `*args, **kwargs` payload -> the result from `target()`
        '''

        self.targets: list[Callable] = targets if common.isIterable(targets) else [targets] # type: ignore
        self.callbacks = callbacks
        self.results = {}
        self.threads: list[SingleThread] = []
        self.lock = threading.Lock()
        self._die: bool = False
        super().__init__()

    def _captureResult(self, target, result):
        with self.lock:
            self.results[target] = result

    def kill(self):
        '''This does not exactly kill the threads, but will prevent them from executing callbacks'''

        self._die = True

    @debug.timing
    def start(self) -> None:
        '''Starts all specified threads. Blocks until completed and all callbacks have finished'''

        console.debug('Starting {} thread(s)'.format(len(self.targets)), timestamp=True) # type: ignore

        target: Callable
        for target in self.targets: 
            thread = SingleThread(
                target=target,
                callbacks=self._captureResult
            )
            thread.start()
            self.threads.append(thread)

        # Wait for threads to complete
        console.debug('Waiting for thread(s) to complete', timestamp=True)
        while not self._die:
            if any([thread.is_alive() for thread in self.threads]):
                time.sleep(0.1)
            else:
                break

        # for thread in self.threads:
        #     thread.join()

        if self._die:
            for thread in self.threads:
                thread.kill()
            return

        console.debug('Finished', timestamp=True)

        if self.callbacks:
            if not common.isIterable(self.callbacks):
                self.callbacks = [self.callbacks]

            console.debug('Executing {} callback(s)'.format(len(self.callbacks)), timestamp=True)  # type: ignore

            callback: Callable
            for callback in self.callbacks: # type: ignore
                callback(self.results)