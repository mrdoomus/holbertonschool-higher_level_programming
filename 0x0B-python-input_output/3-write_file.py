#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Writes certain text in a file
    :param filename: Name of the file
    :param text: Text desired to write in file
    """
    with open(filename, 'w', encoding='utf-8') as fw:
        return fw.write(text)
    """with open(filename, 'r') as fr:
        nb_chars = len(fr.read())
        return nb_chars"""
