#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle


class test_base(unittest.TestCase):
    """ Tests for the base class"""

    @classmethod
    def setUpClass(self):
        print('Start up!')
        self.test = Base()

    def test_base_init(self):
        """Checks instantiation of Base Class"""
        self.assertEqual(self.test.id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(50).id, 50)

    def test_to_json_string(self):
        """Checks to_json_string method of Base Class"""
        list_dict = [Base(1).__dict__]
        self.assertEqual(Base.to_json_string(list_dict), '[{"id": 1}]')
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string(self):
        """Checks from_json_string method of Base Class"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string('[]'), [])
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{"id": 1}])
