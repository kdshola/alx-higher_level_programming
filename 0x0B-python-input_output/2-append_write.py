#!/sr/bin/python3
"""
    append_write function module
"""


def append_write(filename="", text=""):
    """ A funtion that appends text to a file
    Args:
        filename (str): name of file to read
        text (str): string to append to file
    Returns:
        int: number of characters added to file
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
