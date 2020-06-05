#!/usr/bin/python3
""" This module defines number_of_lines"""


def number_of_lines(filename=""):
    """ returns the number of lines in a text file """
    with open(filename, encoding="UTF8") as file:
        count = 0
        for line in file:
            count += 1
        return count
