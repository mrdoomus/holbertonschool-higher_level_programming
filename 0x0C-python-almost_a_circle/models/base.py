#!/usr/bin/python3
""" Module of Base """
from json import dumps, loads


class Base:
    """
    Base class for classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes args """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns json string of a dictionary """
        if list_dictionaries:
            return dumps(list_dictionaries)
        return []

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes a json string to a json file """
        new_list = []
        new_file = cls.__name__ + '.json'
        print(new_file)
        if list_objs:
            new_list = [data.to_dictionary() for data in list_objs]
        with open(new_file, 'w', encoding='utf-8') as f:
            f.write(Base.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """ Return loaded list from json string """
        if json_string:
            return loads(json_string)
        return []
