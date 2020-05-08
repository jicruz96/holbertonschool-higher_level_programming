#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        num = max(i for i in a_dictionary.values())
        for i in a_dictionary:
            if a_dictionary[i] == num:
                return i
    else:
        return None
