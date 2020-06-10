#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestCases(unittest.TestCase):
    """ Tests for the base class"""

    def test_Base(self):
        """Checks creation of Base Class"""
        self.assertAlmostEqual(Base(20).id, 20)

    def test_validate_int(self):
        """ Checks Base.validate_int """
        try:
            Base.validate_int("test", "test")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_validate_non_negative(self):
        """ Checks Base.validate_non_negative """
        try:
            Base.validate_non_negative("test", -1)
        except Exception as e:
            self.assertIsInstance(e, ValueError)

    def test_validate_positive(self):
        """ Checks Base.validate_positive """
        try:
            Base.validate_positive("test", 0)
        except Exception as e:
            self.assertIsInstance(e, ValueError)

    def test_Rectangle(self):
        """Checks creation of Rectangle Class"""
        a = Rectangle(3, 4)
        self.assertAlmostEqual(a.width, 3)
        self.assertAlmostEqual(a.height, 4)

    def test_area(self):
        """ checks area method of Rectangle Class """
        self.assertAlmostEqual(Rectangle(3, 4).area(), 12)
