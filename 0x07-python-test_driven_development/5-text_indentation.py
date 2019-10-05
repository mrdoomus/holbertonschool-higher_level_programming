#!/usr/bin/python3
def text_indentation(text):
    """
    text_identation - Prints a text with 2 new lines after : . ?
    @text: Given text to indent
    """

    if text == "":
        raise TypeError('text must be a string')
    if type(text) is not str:
        raise TypeError('text must be a string')

    cnt = 0
    for i in range(len(text)):
        if i == 0:
            if text[i] == " ":
                continue
        if text[i - 1] in "?.:" and text[i] in "?.:":
            if i != 0:
                print()
                print()
            print(text[i], end='')
        elif text[i - 1] in "?.:":
            print()
            print()
            continue
        else:
            print(text[i], end='')
