#!/usr/bin/python3
"""
Checks if obj is exactly a_class or not
"""


def is_same_class(obj, a_class):
    """
    Checks if obj is instance of a specified class
    :param obj: Object
    :param a_class: Class
    :return: True if is exactly instance, False otherwise
    """
    if type(obj) is a_class:
        return True
    else:
        return False
