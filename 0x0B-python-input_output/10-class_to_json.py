#!/usr/bin/python3
""" Defines class_to_json method """


def class_to_json(obj):
    """ Returns JSON representation of all objects in a class """
    return obj.__dict__
