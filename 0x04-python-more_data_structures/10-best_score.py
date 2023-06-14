#!/usr/bin/python3
# 10-best_score.py
def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    if a_dictionary is None or not isinstance(a_dictionary, dict):
        return None
    key = 'key'
    max_value = 0
    for k, v in a_dictionary.items():
        if v >= max_value:
            max_value = v
            key = k
    if key != 'key':
        return key
    else:
        return None
