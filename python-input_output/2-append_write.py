#!/usr/bin/python3
"""Shebang"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file"""

    with open(filename, mode="w", encoding="utf-8") as f:
        nb_characters = f.write(text)
    return nb_characters
