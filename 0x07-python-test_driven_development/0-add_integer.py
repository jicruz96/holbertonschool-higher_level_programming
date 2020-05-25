#!/usr/bin/python3
"""
This module defines add_integer, a function that returns the sum of 2 integers
If the arguments are floats, they are converted to integers before addition.
The function returns a Type Error if any arguments are not ints or floats.
"""


def add_integer(a, b=98):
    """
    Returns sum of two numbers.
    If one number is inputted, it returns the number plus 98
    """
    if type(a) is float or type(a) is int:
        if type(b) is float or type(b) is int:
            return int(a) + int(b)
        raise TypeError('b must be an integer')

    raise TypeError('a must be an integer')
