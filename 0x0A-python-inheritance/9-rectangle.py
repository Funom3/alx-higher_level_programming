#!/usr/bin/python3
"""module 9-rectangle
creates a rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle"""

    def __init__(self, width, height):
        """initialize the new rectangle
        Args:
            width (int): the width
            height (int): the height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """return the print() and the str() representation"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
