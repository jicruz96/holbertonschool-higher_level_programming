#!/usr/bin/python3
""" Defines BaseGeometry class """


class BaseGeometry:
    """ Base class for geometric shapes """
    pass

    def area(self):
        """ Returns area of shape """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
