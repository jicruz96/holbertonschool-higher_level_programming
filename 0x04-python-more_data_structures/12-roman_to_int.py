#!/usr/bin/python3
def roman_to_int(roman_string):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev = 0
    sum = 0
    if type(roman_string) is str:
        for i in roman_string:
            if val[i] > prev:
                prev *= -1
            sum += prev
            prev = val[i]
    return sum + prev
