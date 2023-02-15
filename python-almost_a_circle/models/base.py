#!/usr/bin/python3
""" Base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Function that returns the json string representation"""
        st = []
        if not list_dictionaries:
            return st
        return json.dumps(list_dictionaries)
