from __future__ import annotations

import os
import typing
import datetime
from proxi import dev
from proxi import config
from proxi import ui
from . import debugSystemTime_ui as window
from . import debugSystemTime_css as css

dev.reloadModules([
    # 'proxi.models', # must come first
    ui, # must come before `window` and `css`
    config,
    window, 
    css,
    'proxi.ui.wrappers.windowBase', 
    'proxi.ui.wrappers.mainWindow'
])

from proxi.ui.wrappers.mainWindow import QtMainWindowWrapper
from PySide6 import (
    # QtGui,
    # QtCore,
    QtWidgets
)


class Window(QtMainWindowWrapper):
    def __init__(self, parent=None):

        if typing.TYPE_CHECKING:
            self.ui = window._TypeHint()

        self.syncStartTime: datetime.datetime|None = None
        self.systemTimeDelta: datetime.timedelta|None = None
        self.systemTimeCounter: float = 0
        self.unrealTickTimeCounter: float = 0
        self.ticks: list[float] = []
        self.maxTicksDisplayed = 40

        super().__init__(
            uiClass = window.Ui_MainWindow,
            prefsPath = config.getUiPrefsPath('debugSystemTime'),
            opacitySlider = False,
            parent = parent
        )


    def _setup(self):
        '''UI is compiled, but not yet displayed'''

        # Connections
        self.ui.reset.clicked.connect(self.resetTimers)

        # Menu triggers
        self.ui.menu_view_reset.triggered.connect(self.resetWindow)
        self.ui.menu_developer_reload_stylesheet.triggered.connect(self._setStyleSheet)

    def _initUi(self):
        '''UI has been displayed, ready for content'''

        self._setStyleSheet()
        self.resetTimers()

    def _setStyleSheet(self):
        '''Set stylesheet overrides'''

        dev.reloadModules([css])

        self.setStyleSheet(ui.UNREAL_APP.styleSheet() + css.STYLESHEET.format(**os.environ))
        QtWidgets.QApplication.instance().processEvents()

    def eventTick(self, delta_seconds, forceUpdate=False):
        '''Event tick from Unreal has been received'''

        now = datetime.datetime.now()
        self.syncStartTime = self.syncStartTime or now
        self.systemTimeDelta = now - self.syncStartTime
        self.systemTimeCounter = self.systemTimeDelta.total_seconds()
        self.unrealTickTimeCounter += delta_seconds
        self.ticks.insert(0, delta_seconds)
        diff = abs(self.systemTimeCounter - self.unrealTickTimeCounter)

        # Output labels
        self.ui.system_time.setText(f'{self.systemTimeCounter:.3f}')
        self.ui.unreal_time.setText(f'{self.unrealTickTimeCounter:.3f}')
        self.ui.difference.setText(f'{diff:.3f}')
        self.ui.running_time.setText(f'{self.systemTimeDelta}')

        # Truncate and output ticks list
        if len(self.ticks) > self.maxTicksDisplayed:
            self.ticks = self.ticks[:self.maxTicksDisplayed]

        self.ui.ticks.setPlainText('\n'.join([f'{x}' for x in self.ticks]))

    def resetTimers(self):
        self.syncStartTime = None
        self.systemTimeCounter = 0
        self.unrealTickTimeCounter = 0
        self.ticks = []
