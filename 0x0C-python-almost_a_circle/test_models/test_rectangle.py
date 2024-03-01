#!/usr/bin/python3
"""unittest module for rectangle module"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import sys


class Test_Rectangle(unittest.TestCase):
    """ represent test class for Rectangl"""
    def test_with_input(self):
        """ test with input width, hight, x and y, and id"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_with_noinput(self):
        """ test with noinput"""
        with self.assertRaises(TypeError):
            r2 = Rectangle()

    def test_with_more_input(self):
        """ test with many input"""
        with self.assertRaises(TypeError):
            r2 = Rectangle(1, 2, 3, 4, 5, 6)

    def test_with_one_input(self):
        """ test with one input"""
        with self.assertRaises(TypeError):
            r2 = Rectangle(1)

    def test_isInstance(self):
        """ test the instance is type Base"""
        r2 = Rectangle(1, 1)
        self.assertIsInstance(r2, Base )

    def test_is_privat(self):
        """ test if private is instance'attriubut"""
        r3 = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            xis = r3.__x

class Test_setter(unittest.TestCase):
    """ test setter """
    def test_width(self):
        """test setter width """
        r = Rectangle(1, 2)
        r.width = 3
        self.assertEqual(r.width, 3)

    def test_width_with_wronginput(self):
        """ test wrong type"""
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r.width = "wrong_in_put"

    def test_width_ngv(self):
        """ test width with negative"""
        r = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            r.width = -3

    def test_height(self):
        """ test setter to height"""
        r = Rectangle(1, 2)
        r.height = 3
        self.assertEqual(r.height, 3)

    def test_with_wrong_height(self):
        """ test with wrong input to height"""
        r = Rectangle(1, 4)
        with self.assertRaises(TypeError):
            r.height = "wrong_height"

    def test_height_ngv(self):
        """ test hieght with negative"""
        r = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            r.height = -3

    def test_x(self):
        """ test setter to x"""
        r = Rectangle(1, 2)
        r.x = 5
        self.assertEqual(r.x, 5)

    def test_x_wronginput(self):
        """ wrong value to x"""
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r.x = "wrongvalue"
	
    def test_x_ngv(self):
        """ test x with negative"""
        r = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            r.x = -3

    def test_y(self):
        """ test setter to y"""
        r = Rectangle(1, 2)
        r.y = 5
        self.assertEqual(r.y, 5)

    def test_y_wronginput(self):
        """ wrong value to y"""
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r.y = "wrongvalue"

    def test_y_neg(self):
        """ test y with negative"""
        r = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            r.y = -3

class Test_area(unittest.TestCase):
    """ class to test area()"""
    def test_area(self):
        """ test area with input to width and height"""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area_witharg(self):
        """ tes area() with argument"""
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r.area(3)

class Test_Display(unittest.TestCase):
    """ test clast to test display()"""
    def test_display(self):
        """ test display with right input"""
        r = Rectangle(2, 1, 3, 4)
        captured = io.StringIO()
        from_stdout = sys.stdout
        sys.stdout = captured
        r.display
        self.assertIn(captured.getvalue(), "##")
        sys.stdout = from_stdout 
