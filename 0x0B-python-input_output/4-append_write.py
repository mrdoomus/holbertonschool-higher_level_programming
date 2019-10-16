#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Writes certain text in a file
    :param filename: Name of the file
    :param text: Text desired to write in file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
        """nb_chars = len(text)
        return nb_chars"""
