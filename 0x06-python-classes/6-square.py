#!/usr/bin/python3
class Square:
    """Square - defines a square checks if its a digit >= 0
    size - changes private size value
    position - coordinates of the square
    area - returns the current square area
    my_print - prints in stdout the square with chars # in a coordinate"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

        if type(position) is not tuple or len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

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
            for newline in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for spaces in range(self.__position[0]):
                    print(" ", end='')
                for column in range(self.__size):
                    print("#", end='')
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value
