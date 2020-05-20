#!/usr/bin/python3
class Square:
    """ Square class. Defines a square with a specific size.

    Args:
        size (int): sets __size

    Attributes:
        __size (int): size of square
    """
    __size = None

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of square

        Returns:
            area of square
        """
        return self.__size * self.__size
