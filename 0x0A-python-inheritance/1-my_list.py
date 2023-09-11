#!/usr/bin/python3
"""
    A module of class My;ist
"""


class MyList(list):
    """ A subclass of the list class """
    def print_sorted(self):
        """ A function that sorts and prints a list in an ascending order
        Returns:
            None
        """
        print(sorted(self))
