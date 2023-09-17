#!/usr/bin/python3
"""
    write_file function module
"""


def write_file(filename="", text=""):
    """ A funtion that writes text to a file
    Args:
        filename (str): name of file to read
        text (str): string to write to file
    Returns:
        int: number of characters written to file
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
