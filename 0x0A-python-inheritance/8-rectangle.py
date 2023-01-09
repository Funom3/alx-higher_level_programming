#!/usr/bin/python3
"""module rectangle
creates a rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents a rectangle
    private instance attributes:
        - width
        - height
    inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """initializes an instance
        Args:
            - width: rectangle width
            - height: rectangle height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
