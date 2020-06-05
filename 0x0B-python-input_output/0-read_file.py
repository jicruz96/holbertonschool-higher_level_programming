#!/usr/bin/python3
"""This module defines read_file"""


def read_file(filename=""):
    """reads a file and prints its contents to stdout"""
    with open(filename, encoding="UTF8") as file:
        for line in file:
            print(line, end="")
