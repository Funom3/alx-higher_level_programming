#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.
    Args:
        filename (str): the name of the file to append
        text (str): the string to append to the file
    Returns:
        the number of the characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
