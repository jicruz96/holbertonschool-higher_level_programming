#!/usr/bin/python3
""" This module defines the say_my_name function """


def say_my_name(first_name, last_name=""):
    """ Prints 'My name is <first_name> <last_name>' """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    if type(last_name) != str:
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))


if __name__ == "__main__":
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)
