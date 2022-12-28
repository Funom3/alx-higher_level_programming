#!/usr/bin/python3
"""
This module is composed by a function that divides the numbers of a matrix
"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix: list of a lists of integer or float
        div: number which divides the matrix
    Returns:
        a new matrix with the result of the division
    Raises:
        TypeError: if the elements of the matrix aren't list
                    if the elements of the list aren't integers or float
                    if div is not an integer or float number
                    if list of the matrix don't have the same size
        ZeroDivisionError: if div is equal to zero
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    msg_type = "Matrix must be a matrix (list of lists) of integers or floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    len_e = 0
    msg_size = "Each row of the matrix must have the same size"
    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(msg_type)

    if len_e != 0 and len(elems) != len_e:
        raise TypeError(msg_size)

    for num in elems:
        if not type(num) in (int, float):
            raise TypeError(msg_type)
        len_e = len(elems)
    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
