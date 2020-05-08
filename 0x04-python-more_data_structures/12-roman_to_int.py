#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or roman_string is "":
        return None

    # Variables and Numeral Values Dictionary:
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev = 0
    sum = 0

    # Go through each letter in the string
    for i in list(roman_string):
        if val[i] > prev:
            prev *= -1
        sum += prev
        prev = val[i]

    return sum + prev
