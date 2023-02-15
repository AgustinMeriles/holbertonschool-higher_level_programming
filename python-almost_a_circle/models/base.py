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
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"

        if list_objs:
            obj_list = [obj.to_dictionary() for obj in list_objs]
        else:
            obj_list = []
        json_str = cls.to_json_string(obj_list)
        with open(filename, "w") as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Function that returns the list of the JSON string representstion"""
        if json_string:
            return json.loads(json_string)
        else:
            v = []
            return v

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        name = cls.__name__
        if name == "Rectangle":
            dummy = cls(1, 1)
        elif name == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Function that returns a list of instances"""
        filename = cls.__name__ + ".json"
        list = []
        try:
            with open(filename, "r") as f:
                json_str = cls.from_json_string(f.read())
                for obj_dict in json_str:
                    list.append(cls.create(**obj_dict))
        except:
            pass
        return list
