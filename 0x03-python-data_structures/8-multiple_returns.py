#!/usr/bin/python3
def multiple_returns(sentence):
    c = None
    strlen = len(sentence)
    if strlen:
        c = sentence[0]
    return (strlen, c)
