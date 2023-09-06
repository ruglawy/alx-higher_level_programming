#!/usr/bin/python3
"""
    Func
"""


def matrix_divided(matrix, div):
    """ FUNC """
    if type(div) is not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_length = 0
    
    for element in matrix:
        if type(element) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if row_length != 0 and len(element) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for el in element:
            if type(num) is not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        row_length = len(element)

    matrix_result = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return matrix_result
