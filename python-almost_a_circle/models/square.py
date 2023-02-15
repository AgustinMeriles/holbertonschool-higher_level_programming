#!/usr/bin/python3
"""New class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Initialization of the class Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Definition"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        id = self.id
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        return ("[Square] ({}) {}/{} - {}".format(id, x, y, w, h, h))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.__width = value
        self.__height = value
