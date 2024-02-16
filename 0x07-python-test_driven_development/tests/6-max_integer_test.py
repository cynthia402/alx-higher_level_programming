#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """represent unittests for max_integer([..])."""

    def test_orderedlist(self):
        """ ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unorderedlist(self):
        """ unordered list of integers."""
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_max_begginning(self):
        """list with a beginning max value."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_emptylist(self):
        """ empty list."""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """list with a single element."""
        self.assertEqual(max_integer([8]), 8)

    def test_floats_(self):
        """list of floats."""
        self.assertEqual(max_integer([1.53, 6.33, -9.123, 15.0, 6.0]), 15.0)

    def test_ints_floats(self):
        """ list of ints and floats."""
        self.assertEqual(max_integer([1.53, 15.0, -9, 15, 6]), 15.0)

    def test_empty(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
