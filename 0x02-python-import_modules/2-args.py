#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv)
    print('{:d} argument'.format(argc - 1), 's' if argc != 2 else '',
          '.' if argc is 1 else ':', sep='')
    for i in range(1, argc):
        print('{:d}: {}'.format(i, argv[i]))
