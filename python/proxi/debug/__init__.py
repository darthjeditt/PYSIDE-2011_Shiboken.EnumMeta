# -*- coding: utf-8 -*-
'''Debug module'''

from __future__ import annotations

import time
import proxi.dev as dev
import proxi.console as console

from decorator import decorator



def toggleDebugMode(displayDialog=True) -> bool:
    '''Toggles debug mode on/off and displays an alert (optional), then returns the current status after change'''

    mode = dev.toggleDebugMode()
    if displayDialog:
        wording = 'ON' if mode else 'OFF'
        print('Debug mode', f'Debug mode is now {wording}')

    return mode


def toggleDevMode(displayDialog=True) -> bool|None:
    '''Toggles developer mode on/off and displays an alert (optional), then returns the current status after change'''

    mode = dev.toggleDevMode()
    if displayDialog:
        if mode is None:
            print('Developer mode', 'Developer mode change is not allowed.\n\nIf you required this functionality, please notify the pipeline team.')
        else:
            wording = 'ON' if mode else 'OFF'
            print('Developer mode', f'Developer mode is now {wording}.\n\nThis status is valid for the current session only.')

    return mode


@decorator
def timing(fn, *args, **kwargs):
    '''Timing wrapper. Outputs method call duration to `console.debug`'''

    # def wrap(*args, **kwargs):
    time1 = time.time()
    ret = fn(*args, **kwargs)
    time2 = time.time()

    console.debug('Method {} took {:.3f} seconds'.format(fn.__name__, time2-time1))

    return ret

    # return wrap