#!/usr/bin/python3
""" Defines load_from_file """
import json


def load_from_json_file(filename):
    """ Loads JSON data from file filename """
    with open(filename, 'r', encoding="UTF8") as file:
        return json.load(file)
