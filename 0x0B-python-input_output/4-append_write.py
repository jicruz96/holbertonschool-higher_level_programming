#!/usr/bin/python3
"""This module defines append_write"""


def append_write(filename="", text=""):
    """ appends a string to a text file (UTF8)
    Return: the number of characters written
    """
    with open(filename, 'a', encoding="UTF8") as fp:
        return fp.write(text)
