#!/usr/bin/python3
""" Defines find_peak """


def find_peak(list_of_integers):
    """ returns a peak within a list of integers """

    if list_of_integers is None or len(list_of_integers) is 0:
        return None

    max = list_of_integers[0]
    for int in list_of_integers:
        if int > max:
            max = int
    return max
