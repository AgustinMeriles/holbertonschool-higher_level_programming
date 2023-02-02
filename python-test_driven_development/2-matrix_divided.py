#!/usr/bin/python3
"""function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix \
                    (list of lists) of integers/floats")

    return [[round(element / div, 2) for element in row] for row in matrix]
