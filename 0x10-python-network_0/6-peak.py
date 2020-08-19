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

    # num_of_ints = len(list_of_integers)
    # if num_of_ints == 0:
    #     return None

    # if num_of_ints == 1:
    #     return list_of_integers[0]

    # if num_of_ints == 2:
    #     if list_of_integers[0] > list_of_integers[1]:
    #         return list_of_integers[0]
    #     return list_of_integers[1]

    # prev = list_of_integers[0]
    # l = list_of_integers
    # for i in range(1, num_of_ints - 2):
    #     curr = l[i]
    #     next = l[i + 1]
    #     if curr >= prev and curr >= next:
    #         return curr
    #     prev = curr
    # print('no!')

    # max = list_of_integers[0]
    # for int in list_of_integers:
    #     if int > max:
    #         max = int
    # return max
