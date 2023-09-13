#!/usr/bin/python3
"""
    append_after function module
"""


def append_after(filename="", search_string="", new_string=""):
    """ appends string to line containing a specific string
    Args:
        filename (str): file to append to
        search_string (str): string to search for in file
        new_string (str): new string to append to file
    Returns: None
    """
    with open(filename, "r+", encoding="utf-8") as file:
        n_list = []
        for line in file:
            n_list.append(line)
            if search_string in line:
                n_list.append(new_string)
        file.seek(0)
        file.writelines(n_list)
