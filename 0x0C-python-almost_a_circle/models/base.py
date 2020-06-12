#!/usr/bin/python3
""" Defines Base class """

import json


class Base:
    """ Base class for almost a circle. """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def validate_int(attr, value):
        """ validates integer inputs """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(attr))

    @staticmethod
    def validate_positive(attr, value):
        """ validates that input is positive """
        if value <= 0:
            raise ValueError('{} must be > 0'.format(attr))

    @staticmethod
    def validate_non_negative(attr, value):
        """ validates that input is non_negative """
        if value < 0:
            raise ValueError('{} must be >= 0'.format(attr))

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        if list_objs is not None:
            list_dicts = [x.to_dictionary() for x in list_objs]
        else:
            list_dicts = []
        with open(cls.__name__ + '.json', 'w') as file:
            return file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ returns object loaded from json_string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with attribute values from dictionary """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances from file <class name>.json """
        try:
            with open(cls.__name__ + '.json', 'r') as file:
                dicts = cls.from_json_string(file.read())
                return [cls.create(**d) for d in dicts]
        except FileNotFoundError:
            return []
        except:
            print('unknown exception!')
            return []
