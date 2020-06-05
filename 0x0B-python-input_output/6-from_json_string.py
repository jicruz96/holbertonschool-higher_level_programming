#!/usr/bin/python3
""" Defines from_json_string """
import json


def from_json_string(my_str):
    """ takes a JSON string as input and returns the object"""
    return json.loads(my_str)
