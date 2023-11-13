#!/usr/bin/python3
import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Test class for Square class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_create_square_instance(self):
        """Create new Square instances."""
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(3, 2, 8, 12)
        self.assertEqual(s2.id, 12)
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 8)

    def test_invalid_square_instances(self):
        """Test creating Square instances with invalid arguments."""
        with self.assertRaises(TypeError) as x:
            s = Square("invalid")
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(ValueError) as x:
            s = Square(0)
        self.assertEqual("width must be > 0", str(x.exception))

        with self.assertRaises(TypeError) as x:
            s = Square(5, "invalid")
        self.assertEqual("x must be an integer", str(x.exception))

        with self.assertRaises(ValueError) as x:
            s = Square(5, -1)
        self.assertEqual("x must be >= 0", str(x.exception))

        with self.assertRaises(TypeError) as x:
            s = Square(5, 2, "invalid")
        self.assertEqual("y must be an integer", str(x.exception))

        with self.assertRaises(ValueError) as x:
            s = Square(5, 2, -3)
        self.assertEqual("y must be >= 0", str(x.exception))

    def test_area_method(self):
        """Test the area method of Square."""
        s = Square(4)
        self.assertEqual(s.area(), 16)

        s = Square(3, 2, 3)
        self.assertEqual(s.area(), 9)

    
if __name__ == "__main__":
    unittest.main()

