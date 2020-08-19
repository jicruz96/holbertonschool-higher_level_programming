#!/usr/bin/python3
""" Defines find_peak """


def find_peak(list_of_integers):
    """ returns a peak within a list of integers """

    prev = None
    for int in list_of_integers:
        if prev is not None and prev >= int:
            return prev
        prev = int
    return prev
