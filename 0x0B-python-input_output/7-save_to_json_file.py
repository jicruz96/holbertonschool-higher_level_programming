#!/usr/bin/python3
""" Defines save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """ saves object my_obj to a JSON file filename """
    with open(filename, 'w', encoding="UTF8") as file:
        return json.dump(my_obj, file)
