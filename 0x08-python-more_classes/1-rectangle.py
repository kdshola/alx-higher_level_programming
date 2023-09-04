#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Model of a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes rectangle width and height
        Args:
            width (int): length if a rectangle
            height (int): height of a rectangle
        Returns:
            None
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter of private variable width
        Returns:
        int: width of an instance of the class rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter of private variable width
        Args:
            value (int): height of an instance of the class rectangle
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter of private variable height
        Returns:
            int: height of an instance of the class rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter of private variable height
        Args:
            value (int): height of an instance of the class rectangle
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
