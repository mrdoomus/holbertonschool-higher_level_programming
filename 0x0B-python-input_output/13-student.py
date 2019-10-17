#!/usr/bin/python3


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes arguments
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dict of class
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for i in attrs:
            if i in self.__dict__.keys():
                new_dict[i] = self.__dict__[i]
        return new_dict

    def reload_from_json(self, json):
        """
        Reloads instances of Student from a json
        """
        if len(json) != 0:
            self.first_name = json["first_name"]
            self.second_name = json["last_name"]
            self.age = json["age"]
