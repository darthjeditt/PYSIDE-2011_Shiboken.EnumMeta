# -*- coding: utf-8 -*-
'''Common UI elements and Qt bootstrapping'''

from __future__ import annotations

import os
import sys
import importlib.util as importUtil
from proxi import dev
from proxi import console
import proxi.ui.resources.proxiQtResources as proxiQtResources
# import qt_material
# import proxiStyle_css as css
from PySide6 import QtGui, QtWidgets
from typing import Callable, cast, TYPE_CHECKING
# from importlib.machinery import SourceFileLoader


CURRENT_SCRIPT_LOCATION = os.path.realpath(__file__)

if TYPE_CHECKING:
    from wrappers.windowBase import QtWindowBaseFactory
    QtWindowBase = QtWindowBaseFactory(None)
else:
    QtWindowBase = type


def rebuildUiFiles():
    '''Rebuild all .ui files'''

    console.warning('Rebuilding all .ui files', timestamp=True)
    buildFile = CURRENT_SCRIPT_LOCATION.replace('\\', '/').split('/proxi/ui/')[0] + '/.build/ui.py'
    try:
        spec = importUtil.spec_from_file_location('buildUi', buildFile)
        mod = importUtil.module_from_spec(spec) # type: ignore
        spec.loader.exec_module(mod)
        mod.main()
        console.log('Rebuilds complete', timestamp=True)
    except Exception as e:
        console.error(f'Failed to run build script: {e}', timestamp=True)


# Auto-rebuild UI in debug mode
if dev.DEV_MODE:
    rebuildUiFiles()

console.debug('Rebuild stage complete', timestamp=True)

# Keep list of open window modules, allowing for module reload without resetting
try:
    OPEN_WINDOWS # type: ignore
except NameError:
    OPEN_WINDOWS: dict[QtWindowBase, Callable] = {}

# Ensure we have a QApplication instance
console.debug('Fetching or creating QApplication instance', timestamp=True)
UNREAL_APP = cast(QtWidgets.QApplication, QtWidgets.QApplication.instance()) or QtWidgets.QApplication(sys.argv)
console.debug(f'QApplication instance contains a total of {len(UNREAL_APP.allWidgets())} child widgets', timestamp=True)

# Set default window icon (this uses `proxiQtResources`)
console.debug('Setting Qt prefs', timestamp=True)
dummy = proxiQtResources.qt_resource_name
logo = QtGui.QIcon(":/favicon.png")
UNREAL_APP.setWindowIcon(logo)

# Load and set fonts
console.debug('Adding fonts', timestamp=True)
# qt_material.add_fonts()
defaultFont = QtGui.QFont('Roboto')
defaultFont.setPixelSize(14)
defaultFont.setStyleStrategy(QtGui.QFont.PreferAntialias)
UNREAL_APP.setFont(defaultFont)

# Apply material theme and any global custom style overrides we have
console.debug('Applying base theme', timestamp=True)
# qt_material.apply_stylesheet(UNREAL_APP, theme='dark_bluegrey.xml')
console.debug('Applying custom theme', timestamp=True)
# UNREAL_APP.setStyleSheet(UNREAL_APP.styleSheet() + css.STYLESHEET.format(**os.environ))

console.debug('Module init complete', timestamp=True)