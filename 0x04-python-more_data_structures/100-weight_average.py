#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        basic = sum([x[1] for x in my_list])
        weighted = sum([x[0] * x[1] for x in my_list])
        return weighted / basic
    return 0
