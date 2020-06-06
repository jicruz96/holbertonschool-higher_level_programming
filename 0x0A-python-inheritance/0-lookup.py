#!/usr/bin/python3
""" defines lookup """


def lookup(obj):
    """ returns list of available attributes and methods of an object """
    return list(dir(obj))
