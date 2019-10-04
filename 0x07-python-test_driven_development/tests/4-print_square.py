#!/usr/bin/python3
def print_square(size):
    """
    print_square - Prints a square with the character #
    @size: Size of the square
    """
    if (type(size) is float and size < 0) or type(size) is not int:
        raise TypeError('size must be an integer')
    elif type(size) is int and size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
