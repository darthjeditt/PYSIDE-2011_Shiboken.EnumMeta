# -*- coding: utf-8 -*-
'''Timestamp formatting'''


class TimeFormats:
    '''Time format strings to use with `strptime`'''

    text = '%Y-%m-%d %H:%M:%S' # log-file values and general text
    file = '%Y-%m-%d_%H-%M-%S' # file and folder names
    console = '%H:%M:%S' # console timestamp, when requested by loggin module