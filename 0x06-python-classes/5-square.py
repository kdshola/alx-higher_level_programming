#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """A class that models a square
    Attributes:
        __size (int): size of a square side
    """
    def __init__(self, size=0):
        """Initializes a square's private property
        Args:
            size (int): length of a side of the square
        Returns: None
        """
        self.size = size

    def area(self):
        """Finds area of an instance of a square
        Returns: Area of the object/instance
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter of the field __size
        Returns: Value of square field __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of private field __size
        Args:
            value (int): length of a side of the square
        Returns: None
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints a square
        Returns: None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("#" * self.__size)
