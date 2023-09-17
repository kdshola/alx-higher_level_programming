#!/usr/bin/python3
"""
read_file function module
"""


def read_file(filename=""):
    """ A funtion that reads a file contents
    Args:
        filename (str): name of file to read
    Returns: None
    """
    with open(filename, 'r', encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
