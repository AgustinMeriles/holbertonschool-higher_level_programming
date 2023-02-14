#!/usr/bin/python3
""" Base class"""


class Base:
    """Initialization of class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
