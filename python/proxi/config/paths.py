# -*- coding: utf-8 -*-
'''Paths config'''

import os


class Paths:
    '''Key folder and server paths'''

    userPrefsDir = '{}/Proxi/Unreal'.format(os.getenv('APPDATA').replace('\\', '/').strip('/'))
    pipelineBaseDynamic = '{}'.format(os.path.dirname(__file__)).replace('\\', '/').replace('/proxi/config', '')