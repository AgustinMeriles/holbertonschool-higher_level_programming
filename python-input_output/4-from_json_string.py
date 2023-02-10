#!/usr/bin/python3
"""Shebang"""
import json


def from_json_string(my_str):
    """function that returns an object represented by json string"""
    return json.loads(my_str)
