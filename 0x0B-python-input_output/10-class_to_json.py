#!/usr/bin/python3


def class_to_json(obj):
    """
    Def to show every content of a class
    :param obj: Instance of a Class
    :return: Dictionary description of a class
    """
    return obj.__dict__
