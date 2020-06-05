#!/usr/bin/python3
""" defines pascal_triangle """


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    Note:
        * returns an empty list if n <= 0
    """
    if n <= 0:
        return []

    pascal = [[1]]

    for i in range(n):
        prev = pascal[i]
        next = [prev[x] + prev[x - 1] for x in range(1, i + 1)]
        next.insert(0, 1)
        next.append(1)
        pascal.append(next)

    return pascal


print(pascal_triangle(5))
