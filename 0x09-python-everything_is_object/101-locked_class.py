#!/usr/bin/python3
"""
    A restricted class module
"""


class LockedClass:
    """ A class that limits dynamic creation of its instance """
    __slots__ = "first_name"
