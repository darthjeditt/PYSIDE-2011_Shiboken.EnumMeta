# -*- coding: utf-8 -*-
'''Configuration module'''

from __future__ import annotations

import os
import dev as dev
import common.strings as strings

from .fileTypes import FileTypes
from .paths import Paths


def getUiPrefsPath(uiFilename: str=None, toolName: str=None) -> str:
    '''Get user prefs location for a given UI file/tool

    Args:
        uiFilename (str, optional): Name of UI file (not path, only filename). Defaults to None.
        toolName (str, optional): Tool name. Defaults to None.

    Raises:
        ValueError: You must specify either `uiFilename` OR `toolName`. Neiter was supplied

    Returns:
        str: Full path to .json file
    '''

    if not uiFilename and not toolName:
        raise ValueError('You must specify either `uiFilename` OR `toolName`. Neiter was supplied')

    if uiFilename:
        base = os.path.basename(uiFilename)
        bare = os.path.splitext(base)[0]
    else:
        bare = toolName.replace(' ', '_')

    return '{}/Proxi_{}.{}'.format(Paths.userPrefsDir, bare, FileTypes.json)


def getUiFilePath(pyFile: str) -> str:
    '''Get .ui file path for a given .py file
    
    Returns:
        str: Full path to .ui file
    '''

    return '{}.{}'.format(os.path.splitext(pyFile)[0], FileTypes.qt)
