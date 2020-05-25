#!/usr/bin/python3
""" Defines matrix_divided, a function that divides a matrix by a constant """


def matrix_divided(matrix, div):
    """ Returns a new matrix where all values are divided by div """

    # Variable assignments for readability purposes only.
    err = TypeError
    msg = 'matrix must be a matrix (list of lists) of integers/floats'

    if type(matrix) != list:
        raise err(msg)

    if type(div) not in (int, float):
        raise err('div must be a number')

    try:
        size = len(max(matrix))
        return [[round(i[j] / div, 2) for j in range(size)] for i in matrix]

    except IndexError:
        raise err('Each row of the matrix must have the same size')
    except ZeroDivisionError:
        raise
    except:
        raise err(msg)
