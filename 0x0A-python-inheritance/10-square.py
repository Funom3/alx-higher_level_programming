#!/usr/bin/python3
"""square class module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square
    Private instance attribute size
    Public method area()
    Inherits from Rectangle
    """

    def __init__(self, size):
        """Initializes a Square
        Args:
            - size: squzre size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """method that returns area of square"""

        return self.__size ** 2
