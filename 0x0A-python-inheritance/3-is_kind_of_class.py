#!/usr/bin/python3
""" module is_kind_of_class
finds if the object is an instance of  or
if object is an instance of a class that inherited from the
specific class
"""


def is_kind_of_class(obj, a_class):
    """find if the obj is an instance of a_class or a class
    inherited from a_class
    Args:
        - obj: object to look at
        - a_class: class to evaluate
    Return: True or False
    """

    return isinstance(obj, a_class)
