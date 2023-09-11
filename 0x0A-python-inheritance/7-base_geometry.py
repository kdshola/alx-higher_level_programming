#!/usr/bin/python3
"""
    A module of a class BaseGeometry
"""


class BaseGeometry:
    """ A class BaseGeometry """
    def area(self):
        """ A public instance method
        Returns:
            None
        Raises:
            Exception: with message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ A public instance method that validates an integer
        Args:
            self: An instance of BaseGeometry
            name (str): integer name
            value (int): integer to validate
        Returns:
            None
        Raises:
            TypeError: if name is not an integer integer
            ValueError: if value is less that zero
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
