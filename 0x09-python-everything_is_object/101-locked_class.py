#!/usr/bin/python3
"""Locked class"""


class LockedClass:
    """
    prevent the user from instanciating new LockedClass attributes for anything but class called first_name
    """
    __slots__ = ["first_name"]
