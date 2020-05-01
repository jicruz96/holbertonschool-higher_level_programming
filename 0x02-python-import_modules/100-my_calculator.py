#!/usr/bin/env python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit
if __name__ == "__main__":
    argc = len(argv)

    if argc != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    if argv[2] not in '+-*/':
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    else:
        result = div(a, b)

    print('{:d} {} {:d} = {:d}'.format(a, operator, b, result))
