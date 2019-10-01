#!/usr/bin/python3
class Square:
    """Square - defines a square checks if its a digit >= 0
    area - returns the current square area"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
