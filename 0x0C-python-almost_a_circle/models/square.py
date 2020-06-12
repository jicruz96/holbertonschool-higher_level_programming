#!/usr/bin/python3
""" Defines Square class """

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Args:
            * size (int): size
            * x (int): horizontal length
            * y (int): vertical length
            * id (int): instance id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns string representation of instance """
        s = '[Square] ({}) {}/{} - {}'
        return s.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ size. must be positive int """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updates class attributes.
            if an argument is not keyworded, update in the following order:
                id -> size -> x -> y
        """

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
            return

        attrs = ('id', 'size', 'x', 'y')
        for i in range(len(args)):
            setattr(self, attrs[i], args[i])

    def to_dictionary(self):
        """ returns dictionary representation of instance """
        keys = ['x', 'y', 'id', 'size']
        return {key: getattr(self, key) for key in keys}
