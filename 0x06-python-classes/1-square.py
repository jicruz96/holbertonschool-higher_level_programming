#!/usr/bin/python3
"""
defines a square with a specific size
"""


class Square:
    """ 
    Square class. Defines a square with a specific size.

    Args:
        size (int): sets __size

    Attributes:
        __size (int): size of square

    """
    __size = None

    def __init__(self, size):
        self.__size = size
