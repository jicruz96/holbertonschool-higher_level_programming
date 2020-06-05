#!/usr/bin/python3
""" Defines the class Student """


class Student:
    """ base class for student profiles.

    Args:
        * first_name (str): initializes first_name
        * last_name (str): initializes last_name
        * age (int): initializes age
    Attributes:
        * first_name (str): first name
        * last_name (str): last name
        * age (int): age
    Methods:
        * to_json(): returns JSON representation of class instance

    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ to_json(): returns JSON representation of object """
        return self.__dict__
