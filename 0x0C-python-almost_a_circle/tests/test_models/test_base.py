#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Base_Tests(unittest.TestCase):
    """ Tests for the base class"""

    @classmethod
    def setUpClass(cls):
        print('setUp')
        cls.init = Base()
        cls.dicts1 = cls.init.__dict__
        cls.string = cls.init.to_json_string([cls.dicts1])
        cls.file = 'Base.json'
        cls.dicts2 = cls.init.from_json_string(cls.string)

    def test_base_init(self):
        """Checks instantiation of Base Class"""
        self.assertEqual(self.init.id, 1)
