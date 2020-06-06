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
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns JSON representation of object
        Note:
            if attrs is a list of strings, only attribute names contained in
            the list are returned.
        """
        d = self.__dict__
        try:
            d = {x: d[x] for x in d if x in attrs}
        except:
            pass

        return d

    def reload_from_json(self, json):
        """
        replaces all instance attributes with attributes from json object
        """
        for key in json.keys():
            setattr(self, key, json[key])
