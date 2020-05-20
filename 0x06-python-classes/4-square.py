#!/usr/bin/python3
"""
Defines a square class with a specific size and area
"""


class Square:
    """ 
    Square class. Defines a square with a specific size.

    Args:
        size (int): sets __size

    Attributes:
        __size (int): size of square
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """
        int: size of square

        Note:
            size must be an int greater than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns area of square

        Returns:
            area of square
        """
        return self.__size * self.__size
