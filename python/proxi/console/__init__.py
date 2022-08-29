# -*- coding: utf-8 -*-
'''Console printing library, to provide some structure to stdOut printing. Future: hook up a logger in here'''

from __future__ import annotations

import traceback
import datetime
from proxi import dev as dev
from types import TracebackType
from proxi.config.timeFormats import TimeFormats


# TODO: Set up cloud provider and patch in a structured logger. Eg `Seq` or similar


def log(outputToPrint: str|object, timestamp: bool=False, stacktrace: bool=False, stripTrailingNewlines: bool=True, method: object=None) -> None:
    '''Print to console (string prepended by a PROXi header and some stack info)
    
    Args:
        outputToPrint (string): What to print given the output
        timestamp (bool, optional): Print timestamp?
        stacktrace (bool, optional): Print stacktrace?
        stripTrailingNewlines(bool, optional): Strip trailing newlines?
        method (func): Logging method, if any. Defaults to None, which means `unreal.log`
    '''

    path = ''
    line = -1
    name = ''

    try:
        stack = traceback.extract_stack()

        if not isinstance(outputToPrint, str):
            outputToPrint = '{}'.format(outputToPrint)

        # Ignore certain calling methods (display previous stack member instead)
        ignoreMethods = [
            'log',
            'debug',
            'warning',
            'messagebox',
            'notify',
            'warn',
            'error',
            'wrap'
        ]

        for call in reversed(stack):
            if call.name.lower() in ignoreMethods:
                continue

            path = call.filename.replace('\\', '/')
            line = call.lineno
            name = call.name
            break

        # Format name a bit better
        if name and name != '<module>':
            name += '()'

        # Remove first part of path
        entryPoint = 'proxi/'
        if entryPoint in path:
            index = path.index(entryPoint)
            path = path[index:]

        # Trim trailing newlines if applicable
        if stripTrailingNewlines:
            outputToPrint = outputToPrint.strip()
    except Exception:
        pass

    
    colon = ':' if name else ''

    # logging format
    if timestamp:
        ts = datetime.datetime.now().strftime(TimeFormats.console)
        print('PROXi ({}:{}) -> {} @ {}{} {}'.format(path, line, name, ts, colon, outputToPrint))
    else:
        print('PROXi ({}:{}) -> {}{} {}'.format(path, line, name, colon, outputToPrint))

    if stacktrace:
        stack = traceback.format_exc()
        if stack:
            print('## Stacktrace ##\n{}'.format(stack))


def debug(what: str|object, timestamp: bool=False, stacktrace:bool=False, stripTrailingNewlines:bool=True) -> None:
    '''Execute `console.log` only for debug sessions
    
    Args:
        what (string): What to print
        timestamp (bool, optional): Print timestamp?
        stacktrace (bool, optional): Print stacktrace?
        stripTrailingNewlines(bool, optional): Strip trailing newlines?
    '''

    if dev.DEBUG_MODE:
        log(what, timestamp=timestamp, stacktrace=stacktrace, stripTrailingNewlines=stripTrailingNewlines)


def warning(what: str|object, timestamp: bool=True, stacktrace: bool=False, stripTrailingNewlines: bool=True):
    '''Log a warning
    
    Args:
        what (string): What to print
        timestamp (bool, optional): Print timestamp?
        stacktrace (bool, optional): Print stacktrace?
        stripTrailingNewlines(bool, optional): Strip trailing newlines?
    '''

    log(what, timestamp=timestamp, stacktrace=stacktrace, stripTrailingNewlines=stripTrailingNewlines)


def error(what: str|object, timestamp: bool=True, stacktrace: bool=True, stripTrailingNewlines: bool=True):
    '''Log an error
    
    Args:
        what (string): What to print
        timestamp (bool, optional): Print timestamp?
        stacktrace (bool, optional): Print stacktrace?
        stripTrailingNewlines(bool, optional): Strip trailing newlines?
    '''

    log(what, timestamp=timestamp, stacktrace=stacktrace, stripTrailingNewlines=stripTrailingNewlines)


def printTraceback(tb: TracebackType|None):
    '''Print supplied traceback object'''

    traceback.print_tb(tb)