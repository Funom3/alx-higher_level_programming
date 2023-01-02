#!/usr/bin/python3
"""this function defines a rectangle by a private instance attribute"""


class Rectangle:
    """the __init__ method initialize the values passed to the object
    attributes:
        width: its a private attribute
        height: its a private attribute
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """the height property"""
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
            return self.__width * self.__height

        def perimeter(self):
            if self.__width == 0 or self.__height == 0:
                return
            return 2 * (self.__width + self.__height)

        def _str__(self):
            if self.__width == 0 or self.__height == 0:
                return ""
            rectangle = ""
            for row in range(self.__height):
                for column in range(self.__width):
                    rectangle += "#"
                if row < self.__height - 1:
                    return rectangle
            return rectangle

        def __repr__(self):
            """ returning the string representation of the rectangle"""
            rect = "Rectangle(" + str(self.__width)
            rect += ", " + str(self.__height) + ")"
            return (rect)
