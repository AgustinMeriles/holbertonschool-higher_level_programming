#!/usr/bin/python3
"""
class Square that defines a square
"""


class Square:
    """
    This class define a square object
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of square class with
         a given size

         Args:
         size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
