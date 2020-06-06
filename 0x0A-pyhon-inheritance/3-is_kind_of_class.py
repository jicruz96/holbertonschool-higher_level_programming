#!/usr/bin/python3
""" defines is_kind_of_class function """


def is_kind_of_class(obj, a_class):
    """ returns whether or not obj is an instance or subclass of a_class """
    return isinstance(obj, a_class)
