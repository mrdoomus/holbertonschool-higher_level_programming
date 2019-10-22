#!/usr/bin/python3
""" Module of Rectangle """
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes args """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ Returns area of a rectangle """
        return self.__height * self.__width

    def display(self):
        """ Prints a rectangle  """
        for y_space in range(self.__y):
            print()
        for column in range(self.__height):
            for x_space in range(self.__x):
                print(" ", end='')
            for row in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """Returns a string representation of a Rectangle instance"""
        string = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return string

    def update(self, *args, **kwargs):
        """ Updates values with passed args """
        att = ["id", "width", "height", "x", "y"]
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
        """ Returns the rectangle's dictionary """
        rect_dict = {'x': self.__x, 'y': self.__y, 'id': self.id,
                     'height': self.__height, 'width': self.__width}
        return rect_dict

    @property
    def width(self):
        """Gets width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width with a value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height with a value."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x with a value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Gets y value """
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y with value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
