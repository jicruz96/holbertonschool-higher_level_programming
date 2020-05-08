#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int


def test_roman(roman_number):
    return "{} = {}".format(roman_number, roman_to_int(roman_number))


testlist = ["XX", "XXXIX", "XLIX", "MMMCMXCIX", "", None]

print(list(map(test_roman, testlist)))
