#!/usr/bin/python3
""" Defines print_sorted function """


class MyList(list):
    """ child of list class that includes a sorted_print method """

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        tmp = self.copy()
        tmp.sort()
        return print('{}'.format(str(tmp)))
