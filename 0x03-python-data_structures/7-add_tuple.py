#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    args = [tuple_a, tuple_b]
    vals = [0, 0]
    for i in args:
        for j in range(len(i)):
            vals[j] = vals[j] + i[j]
            if j == 1:
                break
    return vals[0], vals[1]
