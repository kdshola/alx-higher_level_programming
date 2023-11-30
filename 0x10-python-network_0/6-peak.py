#!/usr/bin/python3
""" module for find_peak function """

def find_peak(list_of_integers):
    """ Function that  finds peak in a list of integers
    Args:
        list_of_integers (list): list of intgers
    Returns:
        int: peak integer or none
    """
    if list_of_integers == []:
        return None
    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]
    if length == 2:
        if list_of_integers[0] >= list_of_integers[1]:
            return list_of_integers[0]
        else:
            return list_of_integers[1]
    start = 0
    mid = int(((length - start) // 2) + start)
    if list_of_integers[mid] >= list_of_integers[mid + 1] and\
            list_of_integers[mid] >= list_of_integers[mid - 1]:
                return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
