#!/usr/bin/python3
def roman_to_int(roman_string):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = roman_string                # for readability only
    if s and type(s) is str:
        n = d[s[0]]                 # n = value of 1st letter
        rest = roman_to_int(s[1:])  # rest = value of rest of string
        if s[1:] and n < d[s[1]]:   # if n < value of next letter, negate n
            n = -n
        return n + rest             # return total value
    return 0


"""
ALTERNATE VERSION: LOOPED   -   slightly more readable
def roman_to_int(roman_string):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev = 0
    sum = 0
    if type(roman_string) is str:
        for i in roman_string:
            if d[i] > prev:
                prev *= -1
            sum += prev
            prev = d[i]
    return sum + prev
"""
