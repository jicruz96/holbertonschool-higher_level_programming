#!/usr/bin/python3
"""
This modules has a class and it's a total square
"""


class Square:
    """I'm a total square

    Args:
        size (int): initiates __size

    Attributes:
        __size (int): size of square
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """ I'm DAD..

            I need to be an int and above 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ I raise an exception if value < 0 or not int """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ I compute the area of the square """
        return self.__size ** 2

    def my_print(self):
        """ I print a '__size x __size' square using '#' """
        if self.__size == 0:
            print()
            return
        x = self.__position[0]
        y = self.__position[1]
        row = str(' ' * x + '#' * self.__size)
        for i in range(y):
            print()
        for i in range(self.__size):
            print('{}'.format(row))

    @property
    def position(self):
        """ I return a position tuple that determines printing behavior """
        return self.__position

    @position.setter
    def position(self, value):
        """ I set __position. Value MUST be a tuple of 2 positive ints """
        msg = TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value, tuple) is False:
            raise msg
        if len(value) != 2:
            raise msg
        for i in value:
            if isinstance(i, int) is False:
                raise msg
        if value[0] < 0 or value[1] < 0:
            raise msg
        self.__position = value
