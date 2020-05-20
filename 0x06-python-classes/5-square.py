#!/usr/bin/python3
class Square:
    """ Square class. Defines a square with a specific size.

    Attributes:
        __size (int): size of square
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """int: size of square

        Note:
            size must be greater than 0
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
        """Returns area of square

        Returns:
            area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints a "__size x __size" square using the hash (#) sign"""
        a = self.__size
        if a == 0:
            print()
        else:
            for i in range(a):
                print('{}'.format(str(self.__size * '#')))
