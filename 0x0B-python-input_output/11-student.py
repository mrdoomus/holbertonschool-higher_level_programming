#!/usr/bin/python3


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes arguments
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns the dict of class
        """
        return self.__dict__
