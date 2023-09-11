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

    def area(self):
        """ Finds the area of a class instance
        Returns:
            int: area of a rectanglr objrct
        """
        return self.__width * self.__height

    def __str__(self):
        """ Defines informal representation of a rectangle
        Return:
            str: rectangle description
        """
        return f"[Rectangle] {self.__width :d}/{self.__height :d}"
