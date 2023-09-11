#!/usr/bin/python3
"""
    A module for class Square
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ A subclass of class Rectangle """
    def __init__(self, size):
        """ Public instance method that instantiates an object
        Args:
            size (int): Rectangle width
        Returns:
            None
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Finds the area of a class instance
        Returns:
            int: area of a rectanglr objrct
        """
        return self.__size * self.__size

    def __str__(self):
        """ Defines informal representation of a rectangle
        Return:
            str: rectangle description
        """
        return f"[Square] {self.__size :d}/{self.__size :d}"
