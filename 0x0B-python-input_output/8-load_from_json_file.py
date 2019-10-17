#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file
    :param filename: name of the file
    """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
