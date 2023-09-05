#!/usr/bin/python3
"""
    Module of a function that prints a square with the character #
"""


def print_square(size):
    """ Function that prints a square with the character #

    Args:
        size: size of the square printed
    Returns:
        None
    Raises:
        TypeError: If size is not an integer number
        ValueError: if value is less than zero

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
