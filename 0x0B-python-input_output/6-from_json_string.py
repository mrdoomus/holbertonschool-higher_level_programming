#!/usr/bin/python3
from json import loads


def from_json_string(my_str):
    """
    Decodes to json
    :param my_obj: Parsed obj
    """
    return json.loads(my_str)
