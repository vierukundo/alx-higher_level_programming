#!/usr/bin/python3
# 100-my_int.py
"""class that inherits from int"""


class MyInt(int):
    """representation of class int"""

    def __eq__(self, other):
        """equality magic method"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """ïnequality magic method"""
        return super().__eq__(other)
