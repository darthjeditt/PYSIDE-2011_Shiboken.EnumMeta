# -*- coding: utf-8 -*-
'''QMainWindow wrapper'''

from __future__ import annotations

import proxi.dev as dev
from .windowBase import QtWindowBaseFactory
from PySide6 import QtCore, QtWidgets
from qt_material import QtStyleTools
from typing import Callable


baseClass = QtWindowBaseFactory(QtWidgets.QMainWindow)
class QtMainWindowWrapper(baseClass, QtStyleTools):

    def __init__(self, uiClass: object, prefsPath: str, overrideTitle: str=None, opacitySlider: bool=False, windowSize: QtCore.QSize=None, flushCacheHook: Callable|None=None, parent: QtWidgets.QWidget=None):
        '''`QMainWindow` wrapper with basic scaffolding for Proxi pipeline and Unreal integration

        Args:
            uiClass (object): UIC.EXE compiled output of .ui file
            prefsPath (str): Full path to prefs file
            overrideTitle (str, optional): Window title to override if applicable. Defaults to None, which means "use dialog title from .ui file"
            opacitySlider (bool, optional): Show the automatically inserted opacity slider (bottom of window)?. Defaults to False.
            windowSize (QSize, optional): Specifies the desired window size, instead of using the size from .ui file
            parent (any, optional): Parent window/object. Defaults to None.
        '''

        super().__init__(
            uiClass = uiClass,
            prefsPath = prefsPath,
            overrideTitle = overrideTitle,
            windowSize = windowSize,
            flushCacheHook = flushCacheHook,
            parent = parent
        )

        # Margins for `centralwidget`
        # self.ui.centralwidget.setContentsMargins(20, 20, 20, 10)

        # Spinner
        self._initSpinner()

        # Append opacity slider if applicable
        if opacitySlider:
            self._initOpacitySlider()

        # Hide `Developer` menu if we're not a developer
        # This menu may or may not exist
        if not dev.DEV_MODE:
            try:
                self.ui.menuDeveloper.setTitle('')
            except Exception:
                pass

        # User setup
        self._setup()