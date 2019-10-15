#!/usr/bin/python3
"""
Checks if obj is a_class or not
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is instance of a specified class
    :param obj: Object
    :param a_class: Class
    :return: True if is instance, False otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
