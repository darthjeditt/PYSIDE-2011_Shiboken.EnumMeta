# -*- coding: utf-8 -*-
'''String manipulations and comparisons'''

from __future__ import annotations

import datetime
import console


def __ensureString__(obj: object) -> str:
    '''Force string conversion for any object'''

    return '{}'.format(obj)


def upper(string: str|None) -> str|None:
    '''Convert a string to UPPERCASE. Force str() for all non-None types
    
    Args:
        string (mixed): String or desired string-object

    Returns:
        str|None: Uppercase string object, or passthrough None object. Depends on input
    '''

    if string is None:
        return None

    try:
        return __ensureString__(string).upper()
    except Exception as e:
        console.error(f'Error converting string `{string}` to upper case: {e}')

    return string


def lower(string: str|None) -> str|None:
    '''Convert a string to lowercase. Force str() for all non-None types
    
    Args:
        string (mixed): String or desired string-object

    Returns:
        str|None: Lowercase string object, or passthrough None object. Depends on input
    '''

    if string is None:
        return None

    try:
        return __ensureString__(string).lower()
    except Exception as e:
        console.error(f'Error converting string `{string}` to lower case: {e}')

    return string


def title(string: str|None) -> str|None:
    '''Convert a string to Title case. Force str() for all non-None types
    
    Args:
        string (mixed): String or desired string-like object
    
    Returns:
        str|None: Titlecased string object, or passthrough None object. Depends on input
    '''

    if string is None:
        return None

    try:
        return __ensureString__(string).title()
    except Exception as e:
        console.error(f'Error converting string `{string}` to title case: {e}')

    return string


def lowerFirst(string: str|None) -> str|None:
    '''Converts a string to have its first letter lower-cased. Eg `InpUT` -> `inpUT`
    
    Args:
        string (mixed): String or desired string-like object
    
    Returns:
        str|None: Processed string, or passthrough None object. Depends on input
    '''

    if string is None:
        return None

    try:
        string = __ensureString__(string)
        return string[0].lower() + string[1:]
    except Exception as e:
        console.error(f'Error converting string `{string}` to lower-first: {e}')

    return string


def camelCase(string: str|None) -> str|None:
    '''Convert a string to camelCase. Expects space-separated string. Eg. `InpUT test sTRING` -> `inputTestString`
    
    Args:
        string (mixed): String or desired string-like object
    
    Returns:
        str|None: camelCased string object, or passthrough None object. Depends on input
    '''

    if string is None:
        return None

    try:
        tokens = string.split(' ')
        return tokens[0].lower() + ''.join([x.title() for x in tokens[1:]])
    except Exception as e:
        console.error(f'Error converting string `{string}` to camel case: {e}')

    return string


def compare(string1: str|None, string2: str|None) -> bool|None:
    '''Compare two strings. Force str() for all non-None types. If either object is None, their comparison value is an empty string
    
    Args:
        string1 (mixed): String or desired string-like object
        string2 (mixed): String or desired string-like object
    
    Returns:
        bool|None: True/False result of string comparison, or None on failure (or input error)
    '''

    if string1 is None:
        string1 = ''
    if string2 is None:
        string2 = ''

    try:
        return __ensureString__(string1) == __ensureString__(string2)
    except Exception as e:
        console.error(f'Error comparing strings `{string1}` and `{string2}`: {e}')

    return None


def toInt(string: str|None, defaultValue: int=-1) -> int:
    '''Convert a string object to an integer
    
    Args:
        string (mixed): String or desired string-like object
        defaultValue (int): Default value if `string` doesn't parse to a known number
    
    Returns:
        int: Integer result on success, `defaultValue` on failure
    '''

    if not string:
        return defaultValue

    try:
        return int(string)
    except Exception as e:
        console.error(f'Error converting string `{string}` to int: {e}')

    return defaultValue


def toFloat(string: str) -> float|None:
    '''Convert a string object to a float
    
    Args:
        string (mixed): String or desired string-like object
    
    Returns:
        float|None: Float result on success, None on failure
    '''

    try:
        return float(string)
    except Exception as e:
        console.error(f'Error converting string `{string}` to float: {e}')

    return None


def toStr(obj: str) -> str:
    '''Convert a given object to a string
    
    Args:
        obj (mixed): Object to convert. Works on most built-in simple data types
    
    Returns:
        str|None: String object on success, None on failure
    '''

    return __ensureString__(obj)


def removeNewlines(string: str) -> str|None:
    '''Remove newlines from a string. Replace with a fullstop and a space

    Args:
        string (str): Input string

    Returns:
        str: Output string
    '''

    try:
        return __ensureString__(string).replace('\n', '. ').replace('\r', '')
    except Exception as e:
        console.error(f'Error removing newlines from string `{string}`: {e}')

    return None


def secondsToDuration(seconds: float|int) -> str:
    '''Convert seconds to timespan string like hh:mm:ss (DOES NOT PAD)
    
    Args:
        seconds (float|int): Number of seconds
    
    Returns:
        str: Result, empty on failure
    '''

    result = ''
    try:
        seconds = int(seconds)
        if seconds > 0:
            result = str(datetime.timedelta(seconds=seconds))
    except Exception as e:
        console.error(f'Error converting seconds to duration from input `{seconds}`: {e}')

    return result


def secondsToTimestamp(seconds: float|int) -> str:
    '''Convert seconds to formatted timestamp 00h 00h 00s (PADDED)
    
    Args:
        seconds (float|int): Number of seconds
    
    Returns:
        str: Result, empty on failure
    '''

    result = ''
    try:
        seconds = int(seconds)
        if seconds > 0:
            h, remainder = divmod(seconds, 60*60)
            m, s = divmod(remainder, 60)
            result = '{:02d}h {:02d}m {:02d}s'.format(h, m, s)
    except Exception as e:
        console.error(f'Error converting seconds to timestamp from input `{seconds}`: {e}')

    return result


def isEmpty(string: str, triggerOnNoneString: bool=False) -> bool:
    '''Check if a string is empty
    
    Args:
        string (str): String to check. If type other than str|None is supplied, method will very likely return False
        triggerOnNoneString (bool, optional): Trigger on 'None'? Defaults to False.
    
    Returns:
        bool: True if empty, False if not
    '''

    try:
        if string is None or string.strip() == '':
            return True
        elif triggerOnNoneString and string.strip().lower() == 'none':
            return True
        else:
            return False
    except Exception:
        return False


def isTrue(string: str) -> bool:
    '''Check if a string is True-ish
    
    Args:
        string (str): String to check. Fallback to bool allowed

    Returns:
        bool: True if "True", False otherwise
    '''

    try:
        if isinstance(string, bool):
            return string
        else:
            _string = __ensureString__(string).strip()
            if _string == 'True' or _string == 'true':
                return True
            else:
                return False
    except Exception:
        return False


def sanitizeSlashes(string: str, removeDoubleSlashes: bool=True) -> str:
    '''Sanitize slashes in string, eg. backslashes becomes forward slashes. Optionally remove double slashes
    
    Args:
        string (str): String to process
        removeDoubleSlashes (bool, optional): Remove double slashes? Defaults to True

    Returns:
        str: Processed string. Passthrough on error
    '''

    try:
        if not isinstance(string, str): # type: ignore
            return ''

        _string = string.replace('\\', '/')
        if removeDoubleSlashes:
            _string = _string.replace('//', '/')

        return _string
    except Exception as e:
        console.error(f'Error sanitizing slashes for string `{string}`: {e}')

    return string


def stripEnd(text: str, suffix: str) -> str:
    '''Strip the supplied character(s) from the end of the string. Order matters, this will match sub-string, not iterate over suffixes'''

    if suffix and text.endswith(suffix):
        return text[:-len(suffix)]
    return text


def plural(num: int, singleValue: str, pluralValue: str|None=None) -> str:
    '''Return either `singleValue` or `pluralValue` based on value of `num`. If `pluralValue` is not specified, an `s` suffix is used

    Args:
        singleValue (str): Singular value string. Eg. Butt or Potato
        num (int): How many values are we formatting grammar for?
        pluralValue (str, optional): If supplied, use this value for plural strings. Eg. Potatoes. Defaults to None, which uses the suffix `s`. Eg. Butts

    Returns:
        str: Formatted string
    '''

    if num == 1:
        return singleValue
    else:
        return pluralValue or f'{singleValue}s'

# Alias
grammar = plural


class Formatting:
    '''Various string formatting methods'''

    @classmethod
    def bold(cls, text: str|None) -> str:
        '''Returns a <span> element containing the supplied text, with font weight set to 800'''

        if not text:
            return ''

        return f'<span style="font-weight: 800;">{text}</span>'

    @classmethod
    def semiBold(cls, text: str|None) -> str:
        '''Returns a <span> element containing the supplied text, with font weight set to 500'''

        if not text:
            return ''

        return f'<span style="font-weight: 500;">{text}</span>'

    @classmethod
    def lineBreak(cls, num: int=2, html: bool=True) -> str:
        '''Returns a string containing the specified number of line-breaks, either as html (<br />) or plaintext (\\n)'''

        if html:
            return '<br/>' * num
        else:
            return '\n' * num

    @classmethod
    def framesToTimecode(cls, frameNum: int, framerate: float) -> str:
        '''Returns a timecode string from a given frame number and framerate'''

        if not frameNum or not framerate:
            h = m = s = f = 0
        else:
            h = int(frameNum / 86400)
            m = int(frameNum / 1440) % 60
            s = int((frameNum % 1440) / framerate)
            f = int(frameNum % 1440 % framerate)

        return '{:02d}:{:02d}:{:02d};{:02d}'.format(h, m, s, f)

    @classmethod
    def secondsToTimecode(cls, second: float, framerate: float):
        if not second or not framerate:
            return Formatting.framesToTimecode(0, 0)
        else:
            return Formatting.framesToTimecode(int(second*framerate), framerate)


class Unicode:
    '''Commonly used Unicode characters supported by Roboto'''

    enDash = '\u2013' # –
    emDash = '\u2014' # —
    chevronsRight = '\u00bb' # »
    chevronsLeft = '\u00ab' # «
    hairSpace = '\u200a'
    bullet = '\u2022' # •
    plus = '\u002b' # +
