#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if type(roman_string) is not str:
        return 0
    if len(roman_string) is 0:
        return 0

    current = dic[roman_string[0]]
    rest = roman_to_int(roman_string[1:])

    if rest == 0:
        return current

    if current < dic[roman_string[1]]:
        current *= -1

    total = current + rest
    return total


"""
ALTERNATE VERSION: LOOPED
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev = 0
    sum = 0
    if type(roman_string) is str:
        for i in roman_string:
            if dic[i] > prev:
                prev *= -1
            sum += prev
            prev = dic[i]
    return sum + prev
"""
