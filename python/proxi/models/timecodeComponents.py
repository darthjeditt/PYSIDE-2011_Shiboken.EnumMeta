# -*- coding: utf-8 -*-
'''Data storage for timecode components'''

from __future__ import annotations 

import proxi.config as config
from dataclasses import dataclass
from enum import Enum, auto


class FrameDelimeter(Enum):
    colon = auto()
    semiColon = auto()


@dataclass(order=True)
class TimecodeComponents:
    hours: int
    minutes: int
    seconds: int
    frames: int

    def generateTimecode(self, frameDelimiter: FrameDelimeter|None=None) -> str:
        '''Generate timecode from components in this `TimeCodeComponents` instance

        Args:
            frameDelimiter (FrameDelimeter, optional): Frame delimiter to use between `seconds` and `frames`. Defaults to None, 
                which resolves to whatever is defined in `config.TimeCode.defaultFrameDelimiter`

        Returns:
            str: Timecode string
        '''

        frameDelimiter = frameDelimiter or config.Timecode.defaultFrameDelimiter
        frameDelimiterString = ':' if frameDelimiter == FrameDelimeter.colon else ';'
        return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}{frameDelimiterString}{self.frames:02}'