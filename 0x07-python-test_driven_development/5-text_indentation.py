#!/usr/bin/python3
""" Defines the text_indentation function """


def text_indentation(text):
    """ Adds two newlines after the '?', ',', ':' characters """

    if type(text) != str:
        raise TypeError('text must be a string')

    delims = [".", "?", ":"]
    output = []
    ignore_spaces = False
    a_space = " "

    for char in list(text):

        if char in delims:
            print(char + "\n")
            ignore_spaces = True
            continue

        if ignore_spaces is True:
            if char is a_space:
                continue
            else:
                ignore_spaces = False

        print(char, end='')
