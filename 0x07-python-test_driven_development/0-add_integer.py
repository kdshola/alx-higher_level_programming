#!/usr/bin/python3
"""
    Add two integers module
"""


def add_integer(a, b=98):
    """ Adds two integers and or two floats

    Args:
        a (int/float): first number
        b (int/float): second number
    Returns:
        int/float: The sum of two numbers
    Raises:
        TypeError: If a or b is not an int or float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
