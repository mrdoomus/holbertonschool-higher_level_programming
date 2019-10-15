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
