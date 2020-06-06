#!/usr/bin/python3
""" Defines BaseGeometry class """


class BaseGeometry:
    """ Base class for geometric shapes """
    pass

    def area(self):
        """ Returns area of shape """
        raise Exception('area() is not implemented')
