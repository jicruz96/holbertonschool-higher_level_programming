#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer
list = [5, 4, 6, 3, -1]


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        """ Test for max_integer. """
        self.assertAlmostEqual(max_integer(), None)
        self.assertAlmostEqual(max_integer([5]), 5)
        self.assertAlmostEqual(max_integer(list[: 2]), 5)
        self.assertAlmostEqual(max_integer(list[: 3]), 6)
        self.assertAlmostEqual(max_integer(list[: 4]), 6)
        self.assertAlmostEqual(max_integer(list), 6)
        self.assertAlmostEqual(max_integer([-1, -2, -3]), -1)
