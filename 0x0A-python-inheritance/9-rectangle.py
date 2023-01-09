#!/usr/bin/python3
"""module 9-rectangle
creates a rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle
    Private instances attributes:
        - width
        - height
    Public method area()
    Inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """initialize an instance
        Args:
            width: rectangle width
            height: rectangle height
        """

        self.integer_validator("width", width)
        sef.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """return a formated string"""
        return str("[rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """computes the area of the rectangle instance
        overwrites the area() method from the BaseGeometry
        """

        return self.__width * self.__height
