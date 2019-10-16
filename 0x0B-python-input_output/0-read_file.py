#!/usr/bin/python3
def read_file(filename=""):
    """
    Opens and reads a file printing its content to stdout
    :param filename: Name of the file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
