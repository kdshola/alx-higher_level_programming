#!/usr/bin/python3
"""
    pascal triangle function module
"""


def pascal_triangle(n):
    """ Depicts the pascal tringle of n
    Args:
        n (int): number whose pascal triangle is returned
    Returns:
        list: pascal triangle of n
    """
    if n <= 0:
        return []

    angle = [[1]]
    while len(angle) != n:
        n_angle = angle[-1]
        temp = [1]
        for i in range(len(n_angle) - 1):
            temp.append(n_angle[i] + n_angle[i + 1])
        temp.append(1)
        angle.append(temp)
    return angle
