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
        super().__init__(size, size)

    def area(self):
        """ Finds the area of a class instance
        Returns:
            int: area of a rectangle objrct
        """
        return self.__size * self.__size
