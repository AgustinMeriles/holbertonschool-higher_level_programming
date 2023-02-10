#!/usr/bin/python3
"""Shebang"""


def write_file(filename="", text=""):
    """function that writes a string to a text file"""

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
    with open(filename, mode="r", encoding="utf-8") as f:
        cont = 0
        for x in f:
            for i in x:
                cont = cont + 1
        return cont
