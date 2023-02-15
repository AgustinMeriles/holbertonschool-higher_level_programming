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
        return ("[Square] ({}) {}/{} - {}".format(id, x, y, w))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """function that assign an argument to each attribute"""
        self.args = args
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """FUnction that returs the dictionary representation of a Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
