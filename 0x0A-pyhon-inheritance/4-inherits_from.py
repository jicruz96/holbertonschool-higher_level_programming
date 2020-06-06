#!/usr/bin/python3
""" defines inherits_from function """


def inherits_from(obj, a_class):
    """ returns whether obj is a subclass of a_class """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
