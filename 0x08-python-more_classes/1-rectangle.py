#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): the width of the new rectangle
            Height (int): the height of the new rectangle.
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """the width property"""
            return self.__width

        @width.setter
        def width(self, value):
            """set width attribute"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """the height property"""
            return self.__height

        @height.setter
        def height(self, value):
            """set the height attribute"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
