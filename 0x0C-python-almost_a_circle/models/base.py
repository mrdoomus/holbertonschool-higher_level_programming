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
        if list_dictionaries is None:
            return dumps([])
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes a json string to a json file """
        new_list = []
        file_name = cls.__name__ + '.json'
        if list_objs:
            new_list = [data.to_dictionary() for data in list_objs]
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(Base.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """ Return loaded list from json string """
        if json_string:
            return loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """ Creates an instance of the class """
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 5)
        elif cls.__name__ == "Square":
            dummy = cls(2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Loads a file of dicts to create a list of instances"""
        file_name = cls.__name__ + '.json'
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                new_list = []
                file_dict = f.read()
                if file_dict is None or len(file_dict) == 0:
                    return []
                file_data = cls.from_json_string(file_dict)
                for dictionary in file_data:
                    instance = cls.create(**dictionary)
                    new_list.append(instance)
                return new_list
        except Exception:
            return []
