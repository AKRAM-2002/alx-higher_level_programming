#!/usr/bin/python3
""" unittesting for base class """
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestClassBasse(unittest.TestCase):
    """ Testing for Base Class """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_create_instance_with_id(self):
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)

    def test_create_instance_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_constructor_id(self):
        """Create new instances: check for id."""
        b0 = Base()
        self.assertEqual(b0.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base(0)
        self.assertEqual(b3.id, 0)
        b4 = Base(927)
        self.assertEqual(b4.id, 927)
        b5 = Base(-5)
        self.assertEqual(b5.id, -5)
        b6 = Base(9)
        self.assertEqual(b6.id, 9)


    def test_to_json_string_with_regular_dict(self):
        """Test static method to_json_string with regular dictionary."""
        dictionary_input = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_string_output = Base.to_json_string([dictionary_input])
        self.assertTrue(isinstance(dictionary_input, dict))
        self.assertTrue(isinstance(json_string_output, str))
        self.assertCountEqual(
            json_string_output, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')

        empty_json_string = Base.to_json_string([])
        self.assertEqual(empty_json_string, "[]")

        none_json_string = Base.to_json_string(None)
        self.assertEqual(none_json_string, "[]")


    def test_to_json_string_with_wrong_types(self):
        """Test static method to_json_string with wrong types."""
        with self.assertRaises(TypeError) as x:
            Base.to_json_string(9)
        self.assertEqual("list_dictionaries must be a list of dictionaries", str(x.exception))

        with self.assertRaises(TypeError) as x:
            Base.to_json_string("Hello")
        self.assertEqual("list_dictionaries must be a list of dictionaries", str(x.exception))

        with self.assertRaises(TypeError) as x:
            Base.to_json_string(["Hi", "Here"])
        self.assertEqual("list_dictionaries must be a list of dictionaries", str(x.exception))

        with self.assertRaises(TypeError) as x:
            Base.to_json_string(7.8)
        self.assertEqual("list_dictionaries must be a list of dictionaries", str(x.exception))

        with self.assertRaises(TypeError) as x:
            Base.to_json_string([2, 1, 3, 4])
        self.assertEqual("list_dictionaries must be a list of dictionaries", str(x.exception))

        with self.assertRaises(TypeError) as x:
            Base.to_json_string({1: 'hi', 2: 'there'})
        self.assertEqual("list_dictionaries must be a list of dictionaries", str(x.exception))

        with self.assertRaises(TypeError) as x:
            Base.to_json_string((9, 0))
        self.assertEqual("list_dictionaries must be a list of dictionaries", str(x.exception))

        with self.assertRaises(TypeError) as x:
            Base.to_json_string(True)
        self.assertEqual("list_dictionaries must be a list of dictionaries", str(x.exception))
