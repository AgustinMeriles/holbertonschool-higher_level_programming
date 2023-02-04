#!/usr/bin/python3
"""Shebang"""


class Rectangle:
    """empty class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        char = ""
        if self.__height is 0 or self.__width is 0:
            return char
        for i in range(self.__height):
            for x in range(self.__width):
                char += "#"
            if i != self.__height - 1:
                char += ('\n')
        return char

    def __repr__(self):
        return (f"Rectangle({self.__width:d}, {self.__height:d})")
