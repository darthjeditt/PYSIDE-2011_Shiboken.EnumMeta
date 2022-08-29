# -*- coding: utf-8 -*-
'''Common utilities'''

from __future__ import annotations
from collections.abc import Iterable


def isIterable(candidate: object, collectionsOnly: bool=True, allowStrings: bool=False):
    '''Determine whether an object is iterable or not
    
    Args:
        candidate (mixed): Object that may or may not be iterable
        collectionsOnly (bool): Check for collections only? Eg. disallow pseudo-iterable objects like `str`. Defaults to True

    Returns:
        bool: True if iterable, False if not
    '''

    if not allowStrings and isinstance(candidate, str):
        return False

    if collectionsOnly:
        return isinstance(candidate, Iterable)

    try:
        iter(candidate) # type: ignore
        return True
    except TypeError:
        return False

    return False

def UniqueList(element) -> list:
    '''Makes a list unique

    Returns:
        list: returns a list of unique elements
    '''

    uniqueElementList = []

    uniqueElement = set(element)

    for item in uniqueElement:
        uniqueElementList.append(item)

    return uniqueElementList
