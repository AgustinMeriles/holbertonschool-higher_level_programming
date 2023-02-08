#!/usr/bin/python3
"""Shebang"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define class"""
    def __init__(self, width, height):
        """define function"""

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        print(f"[Rectangle] {self.__width}/{self.__height}")
        return str(self.__width * self.__height)
