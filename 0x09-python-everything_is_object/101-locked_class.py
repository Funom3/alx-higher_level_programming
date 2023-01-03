#!/usr/bin/python3
"""Locked class"""


class LockedClass:
    """
    only allow thew instantiation of attribute called first_name
    """
    __slots__ = ["first_name"]
