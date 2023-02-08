#!/usr/bin/python3
"""Shebang"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define class Square"""

    def __init__(self, size):
        """Initialization"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size
