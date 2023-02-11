#!/usr/bin/python3
"""Shebang"""
import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


f = "add_item.json"
try:
    items = load_from_json_file(f)
except FileNotFoundError:
    items = []

for item in sys.argv[1:]:
    items.append(item)

save_to_json_file(items, f)
