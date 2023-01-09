#!/usr/bin/python3
"""Module containing add_attribute method"""


def add_attribute(obj, name, value):

    """Method checking if attribute can be set and sets
    where possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
