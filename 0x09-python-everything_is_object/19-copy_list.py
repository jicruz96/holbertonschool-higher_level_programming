#!/usr/bin/python3
""" Defines copy_list """


def copy_list(l):
    return l.copy()


my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)
