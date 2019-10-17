#!/usr/bin/python3
from json import dump


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using JSON
    :param my_obj: Object we want to write to
    :param filename: Name of the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return dump(my_obj, f)
