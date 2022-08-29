# -*- coding: utf-8 -*-
'''QDialog wrapper'''

from __future__ import annotations

from .windowBase import QtWindowBaseFactory
from PySide6 import QtCore, QtWidgets
from typing import Callable


baseClass = QtWindowBaseFactory(QtWidgets.QDialog)
class QtDialogWrapper(baseClass):

    def __init__(self, uiClass: object, prefsPath: str, overrideTitle: str=None, opacitySlider: bool=False, windowSize: QtCore.QSize=None, flushCacheHook: Callable|None=None, parent=None):
        '''`QDialog` wrapper with basic scaffolding for Proxi pipeline and Unreal integration

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
            flushCacheHook=flushCacheHook,
            parent=parent
        )

        # Create layout and add loaded widget
        # layout = QtWidgets.QVBoxLayout()
        # layout.setContentsMargins(0, 0, 0, 0)
        # layout.addWidget(self.ui)
        # self.setLayout(layout)

        # Margins
        # self.layout().setContentsMargins(20, 20, 20, 20)

        # Setup status bar (must be accessed later via self.statusBar() in line with how QMainWindow exposes it)
        # self._statusBar = QtWidgets.QStatusBar(self)
        # layout = QtWidgets.QVBoxLayout()
        # layout.setContentsMargins(0, 10, 0, 0)
        # layout.addWidget(self._statusBar)

        #self._statusBar.setSizeGripEnabled(False)
        #self._statusBar.setContentsMargins(10, 4, 10, 4) # Only sets top/bottom for some reason, but still looks okayish
        
        # self.layout().addLayout(layout)

        # Spinner
        self._initSpinner()

        # Append opacity slider if applicable
        if opacitySlider:
            self._initOpacitySlider()

        # User setup
        self._setup()