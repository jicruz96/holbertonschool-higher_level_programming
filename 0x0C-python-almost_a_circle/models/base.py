#!/usr/bin/python3
""" Defines Base class """


class Base:
    """ Base class for almost a circle.

    Args:
        * id (int): initializes id attribute

    Attributes:
        * id (int): id of class
        * __nb_objects (int): tracks number of base class objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def validate_int(attr, value):
        """ validates integer inputs """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(attr))

    def validate_positive(attr, value):
        """ validates that input is positive """
        if value <= 0:
            raise ValueError('{} must be > 0'.format(attr))

    def validate_non_negative(attr, value):
        """ validates that input is non_negative """
        if value < 0:
            raise ValueError('{} must be >= 0'.format(attr))
