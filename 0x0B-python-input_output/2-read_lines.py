#!/usr/bin/python3
""" This module defines read_lines """


def read_lines(filename="", nb_lines=0):
    """ prints n lines of filename to stdout
    prints every line if n <= 0 or n >= total lines in file
    """
    with open(filename, encoding="UTF8") as file:
        if (nb_lines <= 0):
            print(file.read())

        i = 0
        for i in range(nb_lines):
            line = file.readline()
            if line is "":
                break
            print(line, end="")
