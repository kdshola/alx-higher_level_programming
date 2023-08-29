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
        return self.__size ** 2

    @property
    def size(self):
        """Getter of the field __size
        Returns: Value of square __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Stter of private field __size
        Args:
            value (int): length of a side of the square
        Returns: None
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif length < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __lt__(self, other):
        """Compares square sizes
        Args:
            other (Square): second square object
        Returns:
            True if self is smaller in size else False
        """
        return self.size < other.size

    def __le__(self, other):
        """Compares square sizes for less or equal size values
        Args:
            other (Square): second square object
        Returns:
            True if self is smaller or equal in size else False
        """
        return self.size <= other.size

    def __eq__(self, other):
        """Compares square sizes for equal size values
        Args:
            other (Square): second square object
        Returns:
            True if self is equal in size to other else False
        """
        return self.size == other.size

    def __gt__(self, other):
        """Compares square sizes for size value diference
        Args:
            other (Square): second square object
        Returns:
            True if self is greater in size to other else False
        """
        return self.size > other.size

    def __ge__(self, other):
        """Compares square sizes for greater or equal size values
        Args:
            other (Square): second square object
        Returns:
            True if self is greater or equal in size to other else False
        """
        return self.size >= other.size

    def __ne__(self, other):
        """Compares square sizes for size value diference
        Args:
            other (Square): second square object
        Returns:
            True if self size is not equal to other size else False
        """
        return self.size != other.size
