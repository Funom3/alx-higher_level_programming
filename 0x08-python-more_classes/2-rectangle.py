#!/usr/bin/python3
"""a class that defines a rectangle"""


class Rectangle:
    """a rectangle"""
    def __init__(self, wodth=0, height=0):
        """Initializing the rectangle
        Args:
            width: its a private attribute
            height: its a private attribute
        Raises:
            TypeError: if size is not integer
            ValueError: if the size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """the width property"""
        return self.__width

    @width.setter
    def width(self, value):
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the perimeter of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))
