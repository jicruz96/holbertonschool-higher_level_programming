#!/usr/bin/python3
def magic_string():
    magic_string.times = getattr(magic_string, "times", -1) + 1
    return "Holberton, " * magic_string.times + "Holberton"
