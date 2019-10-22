#!/usr/bin/python3
""" Module of Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes args """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of a Rectangle instance"""
        string = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
        return string

    def update(self, *args, **kwargs):
        """ Updates values with passed args """
        att = ["id", "size", "x", "y"]
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i >= len(att):
                    break
                else:
                    setattr(self, att[i], args[i])
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key in att:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the square's dictionary """
        sz_dict = {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
        return sz_dict

    @property
    def size(self):
        """ Gets size value """
        return self.width

    @size.setter
    def size(self, value):
        """ Sets size with a value """
        self.width = value
        self.height = value
