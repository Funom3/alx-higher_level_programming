#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
        Args:
            matrix: a list of int or float
            div: the divider
        Raises:
        TypeError: if not a number
        TypeError: when sizes are different
        TypeError: if div is not an int or float
        ZeroDivisionError: if div is 0
    Returns:
        a new amtrix
    """
    if (not isinstance(matrix, list) or matrix == [] or not all(isinstance(row, list) for row in matrix)
            or

