#!/usr/bin/python3
""" This module defines the Rectangle class """


class Rectangle:
    """ Defines a rectangle with a width and height value

    Args:
        width (int): width of rectangle
        height (int): height of rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ int: defines width of rectangle.

        Note:
            width must be an int and above 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """ int: defines height of rectangle.

        Note:
            height must be an int and above 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """ returns the rectangle area """
        return self.__height * self.__width

    def perimeter(self):
        """ returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ returns string representation of class """
        str = ""
        rows = self.__height
        hashes = self.__width
        if rows == 0 or hashes == 0:
            return str

        for row in range(rows):
            for hash in range(hashes):
                str += '#'
            if row != rows - 1:
                str += '\n'
        return str
