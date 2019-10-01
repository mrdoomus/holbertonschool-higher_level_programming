#!/usr/bin/python3
class Square:
    """Square - defines a square checks if its a digit >= 0
    size - changes private size value
    area - returns the current square area
    my_print - prints in stdout the square with chars #"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end='')
                print()
