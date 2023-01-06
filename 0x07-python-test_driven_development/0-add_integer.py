#!/usr/bin/python3
"""
this module is composed of a function that add two numbers
"""


def add_integers(a, b=98):
    """
    Function that adds two integer or float numbers
    Args:
        a: first number
        b: second number
    Returns:
        the addition of the two given number
    Raises:
        TypeError: if a or b aren't integer or float numbers
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
