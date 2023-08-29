#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """ A class that represents a square
    Attributes:
        __size (int): size of a square side
    """
    def __init__(self, side_length):
        """Initializes a square's private property
        Args:
            side_length (int): length of a side of the square
        Returns: None
        """
        self.__size = side_length
