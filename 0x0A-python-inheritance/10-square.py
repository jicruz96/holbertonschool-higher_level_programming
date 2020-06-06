#!/usr/bin/python3
""" defines Rectangle class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defines squares.

    Args:
        * size (int): initializes size

    Attributes:
        * size (int): side length of square
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size
