#!/usr/bin/python3
"""Defines a class Node of a singly linked list and class SinglyLinkedList"""


class Node:
    """A class Square that models a singly linked list node
    Attributes:
    """
    def __init__(self, data, next_node=None):
        """Initializes a new node
        Args:
            data (int): node data
            next_node (Node): The next node in the list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Fetches node data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets node data
        Args:
            value (int): new node data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Fetches next node of a linked list"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets next node value
        Args:
            value (Node): new node of the linked list
        """
        if value is None:
            self.__next_node = value
            return
        elif not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Models a singly linked list"""
    def __init__(self):
        """Instantiates a singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node into a sorted singly linked list
        Args:
            value (Node): new node to insert into the list
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """defines the string representation of the singly linked list"""
        data = []
        temp = self.__head
        while temp is not None:
            data.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(data))
