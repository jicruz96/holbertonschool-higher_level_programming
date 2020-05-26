#!/usr/bin/python3
""" Defines the text_indentation function """


def text_indentation(text):
    """ Adds two newlines after the '?', ',', ':' characters """

    if type(text) != str:
        raise TypeError('text must be a string')

    ignore_spaces = False

    for this in list(text):

        if this in ".?:":
            print(this + "\n")
            ignore_spaces = True
            continue

        if ignore_spaces is True and this is " ":
            continue

        print(this, end='')
        ignore_spaces = False
