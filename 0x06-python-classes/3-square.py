#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """ A class that models a square
     Attributes:
        __size (int): size of a square side
    """
    def __init__(self, size=0):
        """Initializes a square's private property
        Args:
            size (int): length of a side of the square
        Returns: None
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Finds area of an instance of a square
        Returns: Area of the object/instance
        """
        return self.__size * self.__size
