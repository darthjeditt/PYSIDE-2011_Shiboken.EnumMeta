# -*- coding: utf-8 -*-
'''Wrapper for all Qt window based classes (QDialog|QMainWindow)'''

from __future__ import annotations

# import unreal
import proxi.dev as dev
import proxi.config as config
#import proxi.ui.tools as uiTools
import proxi.console as console
#import proxi.io.userprefs as userprefs
import proxi.common.threads as threads
import proxi.ui as ui
#import proxi.ui.dialogs as dialogs
#import proxi.ui.widgets.spinner as spinner
from PySide6 import QtGui, QtCore, QtWidgets
from typing import Callable, Type, Any, cast, TYPE_CHECKING
#from proxi.models.persistentPrefsMap import (
#    PersistentPrefsMap
#    # PersistentPrefsCondition
#)

# from abc import ABC, abstractmethod

# dev.reloadModules([
#     config,
#     uiTools,
#     userprefs,
#     threads,
#     dialogs,
#     spinner
# ])



# class _QtWindowBaseCore(ABC):
#     '''This can be vastly extended in the future -- just adding a couple of things now to make type hinting easier'''

#     @abstractmethod
#     def addThreadTerminationHook(self, hook: Callable):
#         '''Add a user defined thread termination hook to the global `shutdownThreads` callback'''


def QtWindowBaseFactory(baseType: Type[QtWidgets.QMainWindow|QtWidgets.QDialog]|None):
    '''Generate a `QtWindowBase` class inheriting from the supplied `baseType`'''

    if TYPE_CHECKING or baseType is None:
        _baseType = QtWidgets.QMainWindow
    else:
        _baseType = baseType

    class QtWindowBase(_baseType):

        def __init__(self, uiClass: object, prefsPath: str, overrideTitle: str=None, windowSize: QtCore.QSize=None, flushCacheHook: Callable|None=None, parent: QtWidgets.QWidget=None):
            '''Base class for all window wrappers, containing basic scaffolding for Proxi pipeline and Unreal integration

            Args:
                uiClass (object): UIC.EXE compiled output of .ui file
                prefsPath (str): Full path to  prefs file
                overrideTitle (str, optional): Window title to override if applicable. Defaults to None, which means "use dialog title from .ui file"
                windowSize (QSize, optional): Specifies the desired window size, instead of using the size from .ui file
                flushCacheHook (object, optional): [description]. Defaults to None.
                parent (QtWidgets.QWidget, optional): [description]. Defaults to None.
            '''

            super().__init__(parent)

            self.hasBeenDisplayed = False
            self.prefsPath = prefsPath
            self.prefs: dict[str, Any] = {}
            self.busy = False
            self.busyCallers = 0
            self.spinner = None
            self._needInitUi = True
            self._needSlateParent = True
            self._destroying = False
            self._closing = False
            self._activeThreads: list[threads.EmittingThread] = []
            self._userDefinedThreadShutdownHooks: list = []
            self.tickHandle = None
            self.pyShutdownHandle = None
            self.flushCacheHook = flushCacheHook
            # self.persistentPrefsMapping: list[PersistentPrefsMap] = []
            self.persistentPrefsMapping = []

            # Fetch ShotGrid project ID (if any)
            # self.defaultProject = config.getShotgridProjectId()

            # Setup UI
            self.ui = uiClass() # type: ignore
            self.ui.setupUi(self) # type: ignore

            self.defaultWindowSize = windowSize or self.size()
            self.detaultWindowPos = QtCore.QPoint(100, 100)
            self.defaultWindowGeo = QtCore.QRect(self.detaultWindowPos, self.defaultWindowSize)
            self.defaultWindowTitle = overrideTitle or self.windowTitle()

            # Load prefs (if any)
            # Guarantees entry self.prefs['windowGeo']: QRect
            self.loadPrefs()

            # Set initial geometry
            self.setMinimumSize(250, 200) # Must be set explicitly to a value, otherwise `setGeometry` becomes unreliable
            self.setGeometry(self.prefs['windowGeo']) # type: ignore

            # Override window title if applicable
            if overrideTitle:
                self.setWindowTitle(overrideTitle)

            # Specific low-level config
            self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True) # Delete ALL windows on close. Free up resources, avoid general fuckery
            # self.setAttribute(QtCore.Qt.WA_DeleteOnClose, dev.DEV_MODE)
            # self.setAttribute(QtCore.Qt.WA_DeleteOnClose, False)
            # self._setup() # Call from child class!

        def _threadTaskCallbackHelper(self, result: threads.ThreadResultWrapper) -> None:
            '''Simple helper method to indicate UI is no longer busy after thread complete'''

            # Termination requested?
            if not result or result.teminateRequested or self._closing or self._destroying:
                return

            # Clean up list of active threads
            if not result.sourceThread in self._activeThreads:
                console.error('Source thread for this signal is not in the list of active threads -- this is not good')
            else:
                self._activeThreads.remove(result.sourceThread)

            # Reset busy state
            if result.resetBusyState:
                self.busyCallers =- 1

            if result.resetBusyState and self.busyCallers < 1:
                self.setBusy(False)

            # Deal with errors captured by thread(s)
            if result.error:
                console.printTraceback(result.error.__traceback__)
                # dialogs.error('An error occurred', f'A background thread raised the following error:\n\n{result.error}'.strip(' <br>'), parent=self)

            # Execute callbacks
            if result.callbacks:
                for callback in result.callbacks:
                    if self._destroying or self._closing:
                        return
                    elif callback:
                        callback(result.payload)

        def _registerTickCallback(self) -> None:
            '''Register tick callback with Unreal'''

            # if not self.tickHandle:
            #     self.tickHandle = unreal.register_slate_post_tick_callback(self.eventTick)

        def _unregisterTickCallback(self) -> None:
            '''Unregister tick callback with Unreal'''

            # if self.tickHandle:
            #     unreal.unregister_slate_post_tick_callback(self.tickHandle)
            #     self.tickHandle = None

        def _registerPythonShutdownCallback(self) -> None:
            '''Register Python shutdown callback with Unreal'''

            # if not self.pyShutdownHandle:
            #     self.pyShutdownHandle = unreal.register_python_shutdown_callback(self._pythonShutdownCallback)

        def _unregisterPythonShutdownCallback(self) -> None:
            '''Unregister Python shutdown callback with Unreal'''

            # if self.pyShutdownHandle:
            #     unreal.unregister_python_shutdown_callback(self.pyShutdownHandle)
            #     self.pyShutdownHandle = None

        def _pythonShutdownCallback(self) -> None:
            '''Python is shutting down'''

            self._delete() # Takes care of unregister

        def _delete(self) -> None:
            '''Close and delete this instance'''

            self._unregisterPythonShutdownCallback()
            self._unregisterTickCallback()
            self._removeWindowInstanceFromTracker()
            self._flushCache()
            self._destroying = True
            self._closing = True
            self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
            self.setWindowOpacity(0) # TODO: Find a less dirty hack here
            self.show()
            self.close()

        # Alias
        _destroy = _delete

        def _removeWindowInstanceFromTracker(self) -> None:
            '''Attempt to remove this instance from the global window tracker'''

            console.log(f'Destroying window instance {self}')

            if self in ui.OPEN_WINDOWS:
                try:
                    del ui.OPEN_WINDOWS[self]
                except Exception as e:
                    console.warning(f'Could not delete window instance {self} from global tracker')

        def _flushCache(self) -> None:
            '''Flush attached cache if we have a hook for it'''

            console.log('Flushing cache')

            if self.flushCacheHook:
                try:
                    self.flushCacheHook()
                except Exception as e:
                    console.warning(f'Error flushing cache object: {e}')

        def _setup(self) -> None:
            '''Placeholder: UI is compiled and ready for setup.
            
            This method takes place BEFORE drawing window on screen, and blocks until complete
            '''

        def _setStyleSheet(self) -> None:
            '''Placeholder: User overrides'''

        def _initSpinner(self) -> None:
            '''With multiple inheritance, this construction doesn't work well during init. Call later, at child's convenience'''

            # self.spinner = spinner.QtSpinner(self, True, True)

        def _initOpacitySlider(self) -> None:
            '''Append opacity slider to window layout, if desireable'''

            self.opacitySlider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
            self.opacitySlider.setMinimum(200)
            self.opacitySlider.setMaximum(1000)
            self.opacitySlider.setValue(1000)
            self.opacitySlider.valueChanged.connect(self.opacitySliderChanged)
            opacityLayout = QtWidgets.QHBoxLayout()
            opacityLayout.addWidget(QtWidgets.QLabel('Window opacity:       '))
            opacityLayout.addWidget(self.opacitySlider)
            opacityLayout.setContentsMargins(12,3,12,0)

            if isinstance(self, QtWidgets.QMainWindow):
                self.ui.centralwidget.layout().addLayout(opacityLayout)
            else:
                self.layout().addLayout(opacityLayout)

        def _initUiHook(self) -> None:
            '''Shim between timer call to _initUi and actual implementation. Deal with tracking, etc'''

            # if dev.DEV_MODE:
            #     self._setStyleSheet()

            console.debug('windowbase._initUiHook triggered', timestamp=True)

            if not self._needInitUi:
                console.debug('windowbase._initUiHook aborted because UI has already been initialized')
                return

            self._needInitUi = False
            self.hasBeenDisplayed = True
            self._initUi()

        def _initUi(self) -> None:
            '''Placeholder: UI has been drawn on screen, now is a good time to populate dynamic/delayed data.
            
            This method takes place AFTER drawing window on screen, and blocks until complete
            '''

        def event(self, event: QtCore.QEvent) -> bool:
            '''Low level event handler. Intercept and handle statusTip request here'''

            if event.type() == event.Type.StatusTip:
                if self.busy:
                    return False
                else:
                    self.statusBarMessage(event.tip()) # type: ignore
                    return True

            return super().event(event)

        def eventTick(self, delta_seconds: float) -> None:
            '''Placeholder: event tick from Unreal has been received'''

        def closeEvent(self, event: QtGui.QCloseEvent) -> None:
            '''Dialog is closing'''

            if self._destroying:
                event.accept()
                return

            console.debug('windowbase.closeEvent triggered')

            # if self.busy:
            #     res = dialogs.questionYesNo(
            #         title='Active background process',
            #         message='There\'s currently a process running in the background (Shotgun upload, data sync, etc).\n\nIf you close this window, that process will be terminated. Are you sure you want to proceed?',
            #         parent=self
            #     )
            #     if not res:
            #         event.ignore()
            #         return

            self._closing = True
            self.shutdownThreads()
            self.savePrefs()
            self._unregisterTickCallback()
            self._removeWindowInstanceFromTracker()
            self._flushCache()
            event.accept()
            self._needSlateParent = True

        def showEvent(self, event: QtGui.QShowEvent) -> None:
            '''Dialog is opening'''

            if self._destroying:
                event.accept()
                return

            # self.hasBeenDisplayed = True
            console.debug('windowbase.showEvent triggered', timestamp=True)
            self._closing = False
            event.accept()
            self._registerTickCallback()
            self._registerPythonShutdownCallback()
            QtCore.QTimer.singleShot(20, self._initUiHook)
            # QtWidgets.QApplication.instance().processEvents()

        def showAndActivate(self) -> None:
            '''Show window and attempt to activate it (bring to foreground). Additionally parent the window to Slate'''

            console.debug('windowBase.showAndActivate triggered')

            self.show()
            self.activateWindow()
            self.setWindowState(QtCore.Qt.WindowActive)

            if self._needSlateParent:
                # unreal.parent_external_window_to_slate(self.winId())
                self._needSlateParent = False

        def addThreadTerminationHook(self, hook: Callable) -> None:
            '''Add a user defined thread termination hook to the global `shutdownThreads` callback'''

            console.log(f'Adding thread termination hook {hook} to shutdown callback')
            self._userDefinedThreadShutdownHooks.append(hook)

        def removeThreadTerminationHook(self, hook: Callable) -> None:
            '''Remove user defined thread termination hook from the global `shutdownThreads` callback'''

            if hook in self._userDefinedThreadShutdownHooks:
                console.log(f'Removing thread termination hook {hook} from shutdown callback')
                self._userDefinedThreadShutdownHooks.remove(hook)
            else:
                console.warning(f'Thread termination hook {hook} NOT found in list of shutdown callbacks')

        def shutdownThreads(self) -> None:
            '''Attempt to shutdown all threads/mark them as termination-requested'''

            console.warning('Shutting down all threads')

            for thread in self._activeThreads:
                console.log(f'Requesting termination for `EmittingThread`: {thread}')
                thread.kill()

            for hook in self._userDefinedThreadShutdownHooks:
                console.log(f'Executing user defined thread shutdown hook: {hook}')

                try:
                    hook()
                except Exception as e:
                    console.error(f'Error executing hook: {e}')

        def setBusy(self, busy: bool, busyText: str=None) -> None:
            '''Toggle busy state (and spinner)'''

            if busy:
                if not self.spinner._isSpinning:
                    self.spinner.start()
                if busyText:
                    console.log(busyText)
                    self.statusBarMessage(busyText)
            else:
                self.busyCallers = 0
                self.spinner.stop()
                self.statusBarMessage(None)

            self.busy = busy
            QtWidgets.QApplication.instance().processEvents()

        def opacitySliderChanged(self, value: int) -> None:
            '''Opacity slider `valueChanged` callback: set window opacity'''

            self.setWindowOpacity(value / 1000)

        def statusBarMessage(self, text: str|None, timeout: int=0) -> None:
            '''Set status bar message if we have a status bar

            Args:
                text (str): Text to display. If None or empty, status bar is cleared
                timeout (int): How long to display the message for, given in milliseconds. If 0, the message remains until cleared or overwritten
            '''

            if not self.haveStatusBar():
                return

            if text:
                self.statusBar().showMessage(text, timeout)
                if timeout > 0:
                    console.log(text)
            else:
                self.statusBar().clearMessage()

        def haveStatusBar(self) -> bool:
            '''Does this window instance have a status bar?'''

            return isinstance(self, QtWidgets.QMainWindow)

        def resetWindow(self, *args) -> None:
            '''Reset window preferences'''

            # QtCore.QTimer.singleShot(20, lambda: uiTools.resetWindow(windowInstance=self))

        # def statusBar(self) -> QtWidgets.QStatusBar:
        #     '''Getter for `QStatusBar` widget'''

        #     if isinstance(self, QtWidgets.QMainWindow):
        #         return super().StatusBar()
        #     else:
        #         return self._statusBar

        def threadTask(self, workerMethod: Callable, workerMethodPayload: object=None, callbackMethod: Callable=None, setBusyState=True, resetBusyState=True, busyText: str=None) -> None:
            '''Threaded task wrapper. Will set the UI in a busy-state while thread is running
            
            Args:
                workerMethod (Callable): Method to run in the thread. Eg. http call, etc.
                workerMethodPayload (object): Payload to send to `workerMethod`
                callbackMethod (Callable): Method to run when the thread has finished. Will receive the `workerMethod` reference and `result` payload as arguments (the latter may be anything -> *args, **kwargs)
                setBusyState (bool): Set interal busy state before starting thread? This affects the spinner. Defaults to True 
                resetBusyState (bool): Reset interal busy state after thread completion? This affects the spinner. Defaults to True
                busyText (str, optional): Text to display during busy state
            
            Callback method must be capable of accepting an `*args, **kwargs` payload
            '''

            if setBusyState:
                self.setBusy(True, busyText)

            if resetBusyState:
                self.busyCallers += 1

            thread = threads.EmittingThread(
                target=workerMethod,
                targetPayload=workerMethodPayload,
                callbacks=callbackMethod,
                resetBusyState=resetBusyState,
                parent=self
            )
            thread.finished.connect(self._threadTaskCallbackHelper) # type: ignore
            thread.start()
            self._activeThreads.append(thread)

        def initPersistentPrefsMapping(self) -> None:
            '''Placeholder: User hook to init `self.persistentPrefsMapping`. Only called if object is empty'''

        def _actionPersistentPrefsMapping(self, save: bool) -> None:
            '''Take action on the user defined `self.persistentPrefsMapping` if applicable. 
            
            `self.prefs` are guaranteed to exist at invocation time, but may be empty
            '''

            console.log(f'Actioning persistent prefs mapping. Save={save}')

            # Init persistent prefs mapping if required
            if not self.persistentPrefsMapping:
                console.log('Mapping doesn\'t exist, attempting init')
                self.initPersistentPrefsMapping()

            # Still don't have any? gtfo
            if not self.persistentPrefsMapping:
                console.log('Still don\'t have mapping, aborting')
                return

            console.log(f'Have {len(self.persistentPrefsMapping)} defined maps, processing')
            for m in self.persistentPrefsMapping:
                try:
                    console.debug(f'Processing map with key {m.key}')

                    if save:
                        valueToSave = m.getter()
                        console.debug(f'Value to save is {valueToSave}')

                        # if valueToSave is None or valueToSave == '' and m.saveCondition == PersistentPrefsCondition.OnlyNonEmpty:
                        #     console.debug(f'Aborting save because save condition `{m.saveCondition}` was not met')
                        #     continue
                        # elif valueToSave != True and m.saveCondition == PersistentPrefsCondition.OnlyTrue:
                        #     console.debug(f'Aborting save because save condition `{m.saveCondition}` was not met')
                        #     continue

                        # console.log(f'All conditions met, storing {m.key}={valueToSave} in `self.prefs`')
                        self.prefs[m.key] = valueToSave
                    else:
                        loadedValue = self.prefs.get(m.key)
                        console.debug(f'Loaded value is {loadedValue}')

                        if loadedValue is None:
                            loadedValue = m.default
                            console.debug(f'Setting default value {loadedValue}')

                        if loadedValue is None:
                            console.log('Loaded value is None after applying defaults, aborting')
                            continue

                        # if loadedValue is None or loadedValue == '' and m.loadCondition == PersistentPrefsCondition.OnlyNonEmpty:
                        #     console.debug(f'Aborting save because load condition `{m.saveCondition}` was not met')
                        #     continue
                        # elif loadedValue != True and m.loadCondition == PersistentPrefsCondition.OnlyTrue:
                        #     console.debug(f'Aborting save because load condition `{m.saveCondition}` was not met')
                        #     continue

                        # console.log(f'All conditions met, sending `{loadedValue}` to setter function {m.setter}')
                        m.setter(loadedValue)

                except Exception as e:
                    console.error(f'Error processing persistent prefs map {m}: {e}')

        def loadPrefs(self) -> None:
            '''Load userprefs. Calls user-overridable `loadPrefs` even if no prefs were loaded'''

            # `userprefs.load` can return None to indicate error/missing file. We don't care,
            # and need to maintain `self.prefs` as a `dict`
            # self.prefs = userprefs.load(self.prefsPath) or {}

            # Parse `windowGeo` from components to a QRect
            if 'windowGeo' in self.prefs:
                try:
                    raw: dict[str, int] = self.prefs['windowGeo'] # type: ignore
                    self.prefs['windowGeo'] = QtCore.QRect(raw['x'], raw['y'], raw['width'], raw['height'])
                    console.debug(f'Parsed window geometry from userprefs: {self.prefs["windowGeo"]}')
                except Exception as e:
                    console.log(f'Error parsing window geo from prefs: {e}')
                    console.log('Using default')
                    self.prefs['windowGeo'] = self.defaultWindowGeo
            else:
                console.debug('No window geo in userprefs, using default')
                self.prefs['windowGeo'] = self.defaultWindowGeo

            # self.prefs['windowGeo'] = uiTools.sanitizeWindowGeo(self.prefs['windowGeo'])

            # Init and action persistent prefs mapping
            self._actionPersistentPrefsMapping(save=False)

            # Call user hook
            self.loadedPrefs()

        def loadedPrefs(self) -> None:
            '''Placeholder: Prefs have been loaded (or not), take required action to use stored values. Loaded values are stored in self.prefs (can be empty, never None)'''

        def savePrefs(self) -> bool:
            '''Save userprefs

            Returns:
                bool: True on success, False on error
            '''

            # Sanitize
            if not self.prefs:
                self.prefs = {}

            # User hook
            if self.savingPrefs() is False:
                console.log('Aborting `savePrefs`, user hook `savingPrefs` demands it')
                return False

            # Init and action persistent prefs mapping
            self._actionPersistentPrefsMapping(save=True)

            # Extract current window geometry and break out in components for the JSON serializer
            geo = self.geometry()
            self.prefs['windowGeo'] = {
                'x': geo.x(),
                'y': geo.y(),
                'width': geo.width(),
                'height': geo.height()
            }

            # return userprefs.save(self.prefs, self.prefsPath)

        def savingPrefs(self) -> bool:
            '''Placeholder: Prefs are about to be saved. Make any required adjustments to self.prefs, which will be dumped as JSON on disk

            Returns:
                bool: Return False to force the save process to terminate
            '''
            return True

    return QtWindowBase