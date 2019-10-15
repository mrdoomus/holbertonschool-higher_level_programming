#!/usr/bin/python3
"""
Returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    obj: Object
    return: List of all available attributes
    """
    return dir(obj)
