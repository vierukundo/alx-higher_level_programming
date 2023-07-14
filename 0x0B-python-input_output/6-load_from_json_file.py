#!/usr/bin/python3
# 6-load_from_json_file.py
"""deserialization function"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename) as f:
        return json.load(f)
