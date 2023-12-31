#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """A class that models a square
    Attributes:
        __size (int): size of a square side
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square's private property
        Args:
            size (int): length of a side of the square
            position (int, int): position of the square
        Returns: None
        """
        self.size = size
        self.position = position

    def area(self):
        """Finds area of an instance of a square
        Returns: Area of the object/instance
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter of the field __size
        Returns: Value of square --size
        """
        return self.__size

    @size.setter
    def size(self, length):
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

    @property
    def position(self):
        """Getter of the field __position
        Returns: Value of square position(tuple)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter of private field __size
        Args:
            value (int, int): length of a side of the square
        Returns: None
        """
        if type(position) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(position[0]) is not int or type(position[0]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(position) != 2 or position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """prints a square
        Returns: None
        """
        if self.__size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for j in range(0, self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size, end="")
            print()

    def __str__(self):
        """defines the print representation of a square"""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for j in range(0, self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size, end="")
            if j != self.__size - 1:
                print()
        return ""
