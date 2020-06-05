#!/usr/bin/python3
""" Adds all file arguments to a file add_item.json """
import json
from sys import argv

save = __import__("7-save_to_json_file").save_to_json_file
load = __import__("8-load_from_json_file").load_from_json_file
file = "add_item.json"

try:
    my_list = list(load(file))
except FileNotFoundError:
    my_list = []

my_list += argv[1:]

save(my_list, file)
