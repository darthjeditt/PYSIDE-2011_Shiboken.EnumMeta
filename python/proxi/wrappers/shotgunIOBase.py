# -*- coding: utf-8 -*-
'''Shotgun integration for Synchotron tool'''

from __future__ import annotations

from typing import Callable, TYPE_CHECKING
import proxi.common.threads as threads
import proxi.config as config
import proxi.console as console
import proxi.shotgun as shotgun

from proxi.exceptions import TooManyThreadsError

if TYPE_CHECKING:
    from proxi.ui.wrappers.windowBase import QtWindowBaseFactory
    QtWindowBase = QtWindowBaseFactory(None)
else:
    QtWindowBase = type


class ShotgunIOBase:

    def __init__(self, window: QtWindowBase|None) -> None:
        self.sgProjectId: int = -1
        self._sg: shotgun.ShotgunClient|None = None
        self._sgActiveThread: threads.MultiThreadWrapper|None = None
        # self.window: _QtWindowBaseCore = window

        if window:
            window.addThreadTerminationHook(self.sgKillActiveThread)

    @property
    def sg(self):
        if not self._sg:
            self._sg = shotgun.ShotgunClient()

        return self._sg

    def sgKillActiveThread(self):
        '''Kill the active API thread'''

        if self._sgActiveThread:
            console.warning('Killing all Shotgun threads')
            self._sgActiveThread.kill()

    def sgApiCall(self, targets: Callable|list[Callable], callbacks: Callable|list[Callable]=None):
        '''Wrapper for the `MultiThread` mechanism from `threads` module. Blocks until all targets have completed'''

        console.log('Executing API call to Shotgun', timestamp=True)

         # Do we already have a thread running? That's not good
        if self._sgActiveThread:
            raise TooManyThreadsError(f'A thread is already running in instance {self}. This is undefined behaviour')

        self._sgActiveThread = threads.MultiThreadWrapper(
            targets=targets,
            callbacks=callbacks
        )
        self._sgActiveThread.start() # Blocks
        self._sgActiveThread = None # Releases

        console.log('API call complete', timestamp=True)