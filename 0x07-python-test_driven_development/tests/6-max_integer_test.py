import unittest
import tests.6-max_integer as 6-max_integer

class TestMax_integer(unittest.TestCase):
    def test_max_integer(self):
        t_list = [1, 4, 5, 6, 20, 34]
        self.assertEqual(6-max_integer(t_list), 34)
