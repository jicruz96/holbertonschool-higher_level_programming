#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int


def test_roman(roman_number):
    return "{} = {}".format(roman_number, roman_to_int(roman_number))


testlist = ["MMMCMLXLIX", "XLIX", 'C', "CXL", "VIII", "", None]

response = list(map(test_roman, testlist))
for i in response:
    print(i)
