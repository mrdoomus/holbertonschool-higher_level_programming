#!/usr/bin/python3
"""
BaseGeometry
"""


class BaseGeometry():
    def area(self):
        """
        Raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if value is an integer
        :param name: String
        :param value: Integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Initializes args
        :param width: An integer
        :param height: An integer
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
         Calculates a rectangle's area
         :return Area width * height
         """
        return self.__width * self.__height

    def __str__(self):
        """
         Magic method str, sets behavior when str or print is called
         :return Printing about calculation
         """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    def __init__(self, size):
        """
        Initializes args
        :param size: An integer, size of a square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
