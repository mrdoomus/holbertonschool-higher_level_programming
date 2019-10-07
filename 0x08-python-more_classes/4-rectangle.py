#!/usr/bin/python3
class Rectangle:
    """
    Rectangle - class
    @__width - Width of a rectangle
    @__height - Height of a rectangle
    __init__ - Initializes attributes
    __str__ - Defines behavior for when str() and print()
    __repr__ - return a string representation of the rectangle
    Area - Returns a rectangle's area
    Perimeter - Returns a rectangle's perimeter
    """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def __str__(self):
        square = ""
        if self.__width == 0 or self.__height == 0:
            return square

        for height in range(self.__height):
            for width in range(self.__width):
                square += "#"
            square += '\n'
        square = square[:-1]
        return square

    def __repr__(self):
        class_representation = "{}({:d}, {:d})".format(
            self.__class__.__name__, self.__width, self.__height)
        return class_representation

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
