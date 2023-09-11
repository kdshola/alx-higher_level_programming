#!/usr/bin/python3
"""
    A module for class Rectangle
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ A subclass of class BaseGeometry """
    def __init__(self, width, height):
        """ Public instance method that instantiates an object
        Args:
            width (int): Rectangle width
            height (int): Rectangle height
        Returns:
            None
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width
