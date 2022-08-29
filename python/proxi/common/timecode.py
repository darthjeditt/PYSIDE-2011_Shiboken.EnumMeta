# -*- coding: utf-8 -*-
'''Timecode manipulations'''

from __future__ import annotations 

import math
import proxi.config as config
from proxi.models.timecodeComponents import TimecodeComponents, FrameDelimeter


def generateTimecodeComponents(frameNumber: int, framesPerSecond: float) -> TimecodeComponents:
    '''Generate `TimeCodeComponents` object from a given `frameNumber` and `framesPerSecond`

    Args:
        frameNumber (int): Frame number to generate timecode for
        framesPerSecond (float): FPS value to use for calculations. Eg. 24

    Returns:
        TimeCodeComponents: An object containing the `hours`, `minutes`, `seconds`, frames` components for the calculated timecode
    '''

    framesPerMinute = 60 * framesPerSecond
    framesPerHour = 60 * 60 * framesPerSecond

    hours = (int)(frameNumber / framesPerHour)
    minutes = (int)(frameNumber / framesPerMinute % 60)
    seconds = (int)(frameNumber / framesPerSecond % 60)
    frames = (int)(frameNumber % framesPerSecond)

    return TimecodeComponents(
        hours=hours,
        minutes=minutes,
        seconds=seconds,
        frames=frames
    )


def generateTimecodeString(frameNumber: int, framesPerSecond: float, frameDelimiter: FrameDelimeter|None=None) -> str:
    '''Generate timecode string from a given `frameNumber` and `framesPerSecond`. Shorthand for `TimeCodeComponents.generateTimeCode()`

    Args:
        frameNumber (int): Frame number to generate timecode for
        framesPerSecond (float): FPS value to use for calculations. Eg. 24
        frameDelimiter (FrameDelimeter, optional): Frame delimiter to use between `seconds` and `frames`. Defaults to None,
            which resolves to whatever is defined in `config.TimeCode.defaultFrameDelimiter`

    Returns:
        str: A string containing the formatted timecode. Eg. `hh:mm:ss;ff`
    '''

    return generateTimecodeComponents(
        frameNumber=frameNumber,
        framesPerSecond=framesPerSecond
    ).generateTimecode(
        frameDelimiter=frameDelimiter
    )


def parseTimecodeString(timeCode: str) -> TimecodeComponents|None:
    '''Parse timecode string to `TimeCodeComponents`

    Raises:
        RuntimeError: Unexpected issue while processing regex `str` results to `int`.
            Indicates corrupted timecode pattern in `config.TimeCode.timeCodePattern`

    Returns:
        TimeCodeComponents: TimeCodeComponents: An object containing the `hours`, `minutes`, `seconds`, frames` components of the parsed timecode
    '''

    match = config.Timecode.timecodePattern.match(timeCode)

    if not match:
        return None

    return TimecodeComponents(
        hours=int(match.group(1)),
        minutes=int(match.group(2)),
        seconds=int(match.group(3)),
        frames=int(match.group(4))
    )


def getFrameFromTimecodeComponents(components: TimecodeComponents, framesPerSecond: float) -> int:
    '''Get the frame number from a given timecode represented as `TimeCodeComponents`

    Args:
        components (TimeCodeComponents): Time code components to generate frame number from
        framesPerSecond (float): FPS value to use for calculations. Eg. 24

    Returns:
        int: Calculated frame number, zero base. -1 if error
    '''

    if not components:
        return -1

    clampedValue = math.ceil((components.hours * 60 * 60 * framesPerSecond) + (components.minutes * 60 * framesPerSecond) + (components.seconds * framesPerSecond)) + components.frames
    return int(clampedValue)


def getFrameFromTimecodeString(timeCode: str, framesPerSecond: float) -> int:
    '''Get the frame number from a given timecode represented as `str`

    Args:
        components (TimeCodeComponents): Time code components to generate frame number from
        framesPerSecond (float): FPS value to use for calculations. Eg. 24

    Returns:
        int: Calculated frame number, zero base. -1 if error
    '''

    if not timeCode:
        return -1

    components = parseTimecodeString(timeCode)
    if not components:
        return -1

    return getFrameFromTimecodeComponents(
        components=components,
        framesPerSecond=framesPerSecond
    )