#!/usr/bin/python3
"""
Checks if obj is a subclass or not
"""
from builtins import issubclass, type


def inherits_from(obj, a_class):
    """
    Checks if obj is subclass of a specified class
    :param obj: Object
    :param a_class: Class
    :return: True if is subclass, False otherwise
    """
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    else:
        return False
