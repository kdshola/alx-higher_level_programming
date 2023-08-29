#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Models a square with private a instance attribute
    Attributes:
        __size (int); length of a side of the square
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
