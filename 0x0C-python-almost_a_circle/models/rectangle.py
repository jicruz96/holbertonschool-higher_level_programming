#!/usr/bin/python3
""" Defines Rectangle class """

from models.base import Base
import json


class Rectangle(Base):
    """ Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            * width (int): width
            * height(int): height
            * x (int): horizontal length
            * y (int): vertical length
            * id (int): instance id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width """
        return self.__width

    @width.setter
    def width(self, value):
        Base.validate_int("width", value)
        Base.validate_positive("width", value)
        self.__width = value

    @property
    def height(self):
        """ height """
        return self.__height

    @height.setter
    def height(self, value):
        Base.validate_int("height", value)
        Base.validate_positive("height", value)
        self.__height = value

    @property
    def x(self):
        """ x """
        return self.__x

    @x.setter
    def x(self, value):
        Base.validate_int("x", value)
        Base.validate_non_negative("x", value)
        self.__x = value

    @property
    def y(self):
        """ y """
        return self.__y

    @y.setter
    def y(self, value):
        Base.validate_int("y", value)
        Base.validate_non_negative("y", value)
        self.__y = value

    def area(self):
        """
        returns the area value of the Rectangle instance.
        """
        return self.width * self.height

    def display(self):
        """ prints representation of instance with '#' """
        if self.width == 0 or self.height == 0:
            print()
            return
        row = ' ' * self.x + '#' * self.width
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(row)

    def __str__(self):
        """ returns string representation of instance """
        s = '[Rectangle] ({}) {}/{} - {}/{}'
        return s.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ updates class attributes. """

        if len(args) > 0:
            attrs = ('id', 'width', 'height', 'x', 'y')
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])

        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

        attrs = ('id', 'width', 'height', 'x', 'y')
        for i in range(len(args)):
            setattr(self, attrs[i], args[i])

    def to_dictionary(self):
        """ returns dictionary representation of instance """
        keys = ['x', 'y', 'id', 'width', 'height']
        return {key: getattr(self, key) for key in keys}
