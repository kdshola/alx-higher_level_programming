0-square.py
An empty class Square that defines a square

1-square.py
A class Square that defines a square (based on 0-square.py)
Private instance attribute: size
Instantiation with size (no type/value verification)

2-square.py
A class Square that defines a square (based on 1-square.py)
Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raises a TypeError exception with the message size must be an integer
if size is less than 0, raises a ValueError exception with the message size must be >= 0.

3-square.py
A class Square that defines a square (based on 2-square.py)
Public instance method: def area(self): that returns the current square area

4-square.py
A class Square that defines a square (based on 3-square.py)
Instantiation with optional size: def __init__(self, size=0):

5-square.py
A class Square that defines a square (based on 4-square.py)
Public instance method: def my_print(self): that prints in stdout the square with the character #:
if size is equal to 0, prints an empty line

6-square.py
A class Square that defines a square (based on 5-square.py)
Private instance attribute: position:
property def position(self): to retrieve it
property setter def position(self, value): to set it:
position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers

100-singly_linked_list.py
A class Node that defines a node of a singly linked list.

101-square.py
A class Square that defines a square (based on 6-square.py).

102-square.py
A class Square that defines a square (based on 4-square.py)
Square instance can answer to comparators: ==, !=, >, >=, < and <= based on the square area.
