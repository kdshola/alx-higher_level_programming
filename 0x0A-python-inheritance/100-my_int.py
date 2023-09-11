#!/usr/bin/python3
"""
    A module of class MyInt
"""


class MyInt(int):
    """ A subclass of the integer class """
    def __eq__(self, other):
        """ checks if instance is equal to other
        Returns:
            bool: True if both are not equal else False
        """
        return not int(str(self)) == other

    def __ne__(self, other):
        """ checks if instance is equal to other
        Returns:
            bool: True if both are equal else False
        """
        return not int(str(self)) != other
