#!/usr/bin/python3
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
"""
script that adds all arguments to a Python list, and then save them to a file
"""

try:
    load_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    load_list = []
finally:
    for i in range(1, len(argv)):
        load_list.append(argv[i])
    save_to_json_file(load_list, "add_item.json")
