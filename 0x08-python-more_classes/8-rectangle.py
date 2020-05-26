#!/usr/bin/python3
""" This module defines the Rectangle class """


class Rectangle:
    """ Defines a rectangle with a width and height value

    Args:
        width (int): width of rectangle
        height (int): height of rectangle

    Attributes:
        number_of_instances (int): number of instances of the class
            in existence
        print_symbol: symbol used for string representation of class
            * initialized to '#'
            * can be of any type
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        s = ""
        rows = self.__height
        symbols = self.__width
        if rows == 0 or symbols == 0:
            return s

        for row in range(rows):
            for symbol in range(symbols):
                s += str(self.print_symbol)
            if row != rows - 1:
                s += '\n'
        return s

    def __repr__(self):
        """ returns string representation of command
        that instantiated the object
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """prints a goodbye message upon deletion of object"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
        del self

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
