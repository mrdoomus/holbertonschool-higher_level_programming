#!/usr/bin/python3
from json import dumps


def to_json_string(my_obj):
    """
    Converts to json
    :param my_obj: Parsed obj
    """
    return json.dumps(my_obj)
