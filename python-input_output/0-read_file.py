#!/usr/bin/python3
"""Shebang"""


def read_file(filename=""):
    """Initialize"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
