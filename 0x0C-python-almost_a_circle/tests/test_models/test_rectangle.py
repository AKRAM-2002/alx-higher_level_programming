#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test class for Rectangle class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_create_rectangle_instance(self):
        """Create new Rectangle instances."""
        r1 = Rectangle(5, 10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(3, 7, 2, 8, 12)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 7)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 8)

    def test_invalid_rectangle_instances(self):
        """Test creating Rectangle instances with invalid arguments."""
        with self.assertRaises(TypeError) as x:
            r = Rectangle("invalid", 5)
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r = Rectangle(0, 5)
        self.assertEqual("width must be > 0", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r = Rectangle(5, "invalid")
        self.assertEqual("height must be an integer", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r = Rectangle(5, 0)
        self.assertEqual("height must be > 0", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r = Rectangle(5, 10, "invalid")
        self.assertEqual("x must be an integer", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r = Rectangle(5, 10, -1)
        self.assertEqual("x must be >= 0", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r = Rectangle(5, 10, 2, "invalid")
        self.assertEqual("y must be an integer", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r = Rectangle(5, 10, 2, -3)
        self.assertEqual("y must be >= 0", str(x.exception))

    def test_area_method(self):
        """Test the area method of Rectangle."""
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

        r = Rectangle(3, 8, 2, 3)
        self.assertEqual(r.area(), 24)

if __name__ == "__main__":
    unittest.main()
