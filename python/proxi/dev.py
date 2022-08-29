# -*- coding: utf-8 -*-
'''PROXi module developer methods'''

from __future__ import annotations

import types
import importlib
import os


_DEBUG_FILE = os.path.expanduser(r'~\Documents\unreal-debug')
_DEV_FILE = os.path.expanduser(r'~\Documents\unreal-dev')
DEBUG_MODE = os.path.isfile(_DEBUG_FILE)
DEV_MODE = os.path.isfile(_DEV_FILE)
print(f'Debug mode? {DEBUG_MODE}')
print(f'Developer mode? {DEV_MODE}')


def reloadModules(modules: list[types.ModuleType|str], onlyInDevMode: bool=True):
    '''Reload the specified modules or module paths if we're in DEV mode (optionally forced)'''

    if onlyInDevMode and not DEV_MODE:
        return

    for mod in modules:
        if isinstance(mod, str):
            print(f'Importing module {mod}')
            mod = importlib.import_module(mod)
        print(f'Reloading module {mod.__name__}')
        mod = importlib.reload(mod)


def insertReloadForDev(moduleName) -> str:
    '''Insert reload call in import string if we're in dev mode'''

    if DEV_MODE:
        return f'import importlib; importlib.reload({moduleName}); '
    else:
        return ''


def toggleDebugMode() -> bool:
    '''Toggles debug mode on/off and returns the current status after change (bool)'''

    global DEBUG_MODE

    currentStatus = os.path.isfile(_DEBUG_FILE)
    try:
        if currentStatus:
            os.remove(_DEBUG_FILE)
        else:
            open(_DEBUG_FILE, 'w').close()
    except Exception as e:
        print(f'Error deleting and/or creating debug file tracker: {e}')

    DEBUG_MODE = not currentStatus
    return DEBUG_MODE


def toggleDevMode() -> bool|None:
    '''Toggles dev mode on/off for the CURRENT SESSION ONLY, and returns the current status after change (bool).
    
    If mode change is not allowed, None is returned
    '''
    
    global DEV_MODE

    if not os.path.isfile(_DEV_FILE):
        return None

    DEV_MODE = not DEV_MODE
    return DEV_MODE