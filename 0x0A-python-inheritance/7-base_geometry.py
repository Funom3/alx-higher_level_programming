#!/usr/bin/python3
"""module base_geometry
creates a base geometry class
"""


class BaseGeometry:
    """class with public instance methods"""

    def area(self):
        """raise an exception with message
        'area() is not omplemented'
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validate the values"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
