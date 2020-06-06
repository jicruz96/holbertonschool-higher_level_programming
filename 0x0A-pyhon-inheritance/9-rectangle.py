#!/usr/bin/python3
""" defines Rectangle class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle

    Args:
        * width (int): initializes width
        * height (int): initializes height
    Attributes:
        * width (int): width
        * height (int): height
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns area of shape """
        return self.__width * self.__height

    def __str__(self):
        """ Returns string representation of class """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
