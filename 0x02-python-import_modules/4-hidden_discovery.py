#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":

    imported_names = sorted(dir(hidden_4))

    for name in imported_names:
        if "__" not in name[0:2]:
            print('{}'.format(name))
