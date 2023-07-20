#!/usr/bin/python3
"""Defines unittests for base.py"""


import unittest
from models.base import Base

class base(unittest.TestCase):

    def test_id(self):
        b = Base()
        b1 = Base()
        self.assertEqual(b.id, 1)
        self.assertEqual(b1.id, 2)

if __name__ == "__main__":
    unittest.main()
