#!/usr/bin/python3
""" returns True if the object is exactly an instance of the
 specified class; otherwise False"""


def inherits_from(obj, a_class):
    """Inicialized"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
