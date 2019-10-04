#!/usr/bin/python3
def add_integer(a, b=98):
    """
    add_integer - Adds two integers
    @a: N1
    @b: N2
    Return: The addition
    """
    if type(a) is int or type(a) is float:
        x = int(a)
    else:
        raise TypeError('a must be an integer')

    if type(b) is int or type(b) is float:
        y = int(b)
    else:
        raise TypeError('b must be an integer')

    return x + y
