#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """Creation of the class"""
    def print_sorted(self):
        """Inicialized"""
        new = sorted(self)
        print(new)
