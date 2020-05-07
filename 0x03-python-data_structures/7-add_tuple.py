#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list = [tuple_a, tuple_b]
    sum = [0, 0]
    for i in list:
        if len(i):
            sum[0] += i[0]
            if len(i) > 1:
                sum[1] += i[1]
    return sum[0], sum[1]
