#!/usr/bin/python3
# 4-from_json_string.py
import json
"""deserialization function"""


def from_json_string(my_str):
    """returns an object (Python data structure)
    represented by a JSON string"""
    return (json.loads(my_str))
