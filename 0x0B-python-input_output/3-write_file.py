#!/usr/bin/python3
""" This module defines write_file """


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8)
    Return: the number of characters written
    """
    with open(filename, 'w', encoding="UTF8") as fp:
        return fp.write(text)
