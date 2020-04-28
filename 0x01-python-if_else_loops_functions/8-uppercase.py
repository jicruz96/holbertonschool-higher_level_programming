#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        j = ord(str[i])
        if j > 96 and j < 123:
            print('{:c}'.format(j - 32), end='')
        else:
            print('{:c}'.format(j), end='')
    print()