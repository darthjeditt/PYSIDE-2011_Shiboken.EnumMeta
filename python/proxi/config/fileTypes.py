# -*- coding: utf-8 -*-
'''File types lookup'''

from __future__ import annotations


class FileTypes:
    '''File types: mb, fbx, mov, mp4, etc. For formatted extensions, use the `extensions` object'''

    maya           = 'mb'
    mayaAscii      = 'ma'
    mayaBinary     = maya # alias
    log            = 'log'
    json           = 'json'
    fbx            = 'fbx'
    mobu           = fbx # alias
    png            = 'png'
    jpg            = 'jpg'
    tif            = 'tif'
    tiff           = 'tiff'
    bmp            = 'bmp'
    exr            = 'exr'
    mov            = 'mov'
    mp4            = 'mp4'
    wav            = 'wav'
    qt             = 'ui'


class FileExtensions(object):
    '''Formatted file extensions: .mb, .mp4, etc
    
    Use the .get(<type>) accessor for lookup
    '''

    def __init__(self):
        self.allExtensions: dict[str, str] = {}

        # Straight up dot-extensions
        for key, value in vars(FileTypes).items():
            if not '__' in key:
                self.allExtensions[key] = '.{}'.format(value)

        # Future: add any special file extensions here (not directly derived from `fileTypes`)

    def get(self, typeOrKey):
        '''Get formatted extension for a given type/key. Access `allExtensions` for a full list

        Args:
            typeOrKey (str|mixed): File type or key name to query extension for

        Returns:
            str|None: File extension including period/stop, if found. None otherwise.
        '''

        if typeOrKey in self.allExtensions:
            return self.allExtensions[typeOrKey]
        else:
            return None

    def items(self):
        '''Shorthand for self.allExtensions.iteritems()
        
        Returns:
            dict iterator
        '''

        return self.allExtensions.items()

    # Alias
    iteritems = items