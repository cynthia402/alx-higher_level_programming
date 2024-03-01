#!/usr/bin/python3

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle

class Testbase(unittest.TestCase):
    """ test Base class"""
    def setUp(self):
        print("setUp self")

    def tearDown(self):
        print("tearDown self")

    def test_Base_with_id(self):
        """ test with uniq id"""
        self.assertEqual(Base(3).id, 3)
        self.assertEqual(Base(10).id, 10)
        self.assertEqual(Base(2).id, 2)

    def test_Base_with_None(self):
       """ test with None id value"""
       self.assertEqual(Base(None).id, 1)
       self.assertEqual(Base().id, 2)

    def test_Base_with_float(self):
        """ test with float id value"""
        self.assertEqual(Base(1.5).id, 1.5)
        self.assertEqual(Base(-1.5).id, -1.5)

    def test_Base_with_inf(self):
        """ test with ininity number"""
        infi = Base(float("inf"))
        self.assertEqual(infi.id, float("inf"))
        self.assertEqual(Base(float("-inf")).id, float("-inf"))

    def test_Base_isPrivat_nb_objects(self):
        """ test the class private atribute __nb_objects is not accessable"""
        with self.assertRaises(AttributeError):
            print(Base(2).__nb_objects)

    def test_Base_is_id_public(self):
        """ ensure id is public"""
        change_ = Base(1)
        change_.id = 11
        self.assertEqual(change_.id, 11)

    def test_Base_with_more_arg(self):
        """ test the input morethan expected"""
        with self.assertRaises(TypeError):
            b0 = Base(2, 3).id
            print(b0.id)




class test_to_json_string(unittest.TestCase):
    """ represent a class to test to_json_string func"""
    def test_to_json_string_WithList_dict(self):
        list_dic = [{"a": 97, "b": 98}]
        j = Base()
        j_str =j.to_json_string(list_dic)
        self.assertEqual(j_str, '[{"a": 97, "b": 98}]')

    def test_to_json_string_with_dict(self):
        """ test with input of dictionary"""
        dic = {"a": 97, "name": "abel"}
        j_str = Base.to_json_string([dic])
        self.assertEqual(j_str, '[{"a": 97, "name": "abel"}]')

    def test_with_string(self):
        """ test with string as input"""
        self.assertEqual(Base.to_json_string("abel"), '"abel"')

    def test_with_set(self):
        """ test with set as input and excpect type error"""
        with self.assertRaises(TypeError):
            Base.to_json_string({2, 3})

    def test_with_tuple(self):
        """ test with tuple as input"""
        self.assertEqual(Base.to_json_string((2)), '2')

    def test_with_nested_list(self):
        """ test with nested with lst as input"""
        self.assertEqual(Base.to_json_string([["string"], (2, 3), {"key": "vlaue"}]),
            '[["string"], [2, 3], {"key": "vlaue"}]')

        """ def test_with_bool(self):
        test with bool as input
        self.assertEqual(Base.to_json_string(True),bool(true))
        self.assertFalse(Base.to_json_string(False))
        """

    def test_to_json_string_None_emptyList(self):
        j2 = Base()
        j2_str = j2.to_json_string(None)
        self.assertEqual(j2_str, '[]')
        
        j3 = Base()
        j3_str = j3.to_json_string([])
        self.assertEqual(j3_str, '[]')

    def test_with_more_argu(self):
        """ test with more arguments """
        with self.assertRaises(TypeError):
            Base.to_json_string([2], ["ab"])

    def test_with_no_arg(self):
        """ test with no argument as input"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

class test_save_to_file(unittest.TestCase):
    """ represent test class for sav_to_file func"""
    @classmethod
    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
    
    def test_with_list_ofinstance(self):
        """ test with list of dict"""
        list_dic = [{"key": "value"}]
        s_j =Rectangle(1, 2)
        Rectangle.save_to_file([s_j])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 52)

    def test_with_two_instance(self):
        """ test with two instance of Rectangle"""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(104, len(f.read()))

    def test_with_none(self):
        """ test with None as input"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(str, type(f.read()))

class test_from_json_string(unittest.TestCase):
      """ represent a class for testing from_json_string"""
      def test_with_Json_string(self):
          a = '[{"a": 1, "b": 2}]'
          self.assertEqual(Base.from_json_string(a), [{"a": 1, "b": 2}])

      def test_with_None(self):
          """ test with None as input"""
          self.assertEqual(Base.from_json_string(None), [])

      def test_with_empty(self):
          """ test with no input"""
          with self.assertRaises(TypeError):
              Base.from_json_string()

class test_create(unittest.TestCase):
    """ represent class to test create()"""
    def test_with_dic(self):
        """ test using dic as input"""
        r = Rectangle(1, 2, 3, 4, 5)
        r_dic = r.to_dictionary()
        r2 = Rectangle.create(**r_dic)
        self.assertEqual(str(r2), "[Rectangle] (5) 3/4 - 1/2")

    def test_IsNotEqual(self):
        """ test if new instance is created"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1_dic = r1.to_dictionary()
        new = Rectangle.create(**r1_dic)
        self.assertNotEqual(new, r1)
        self.assertIsNot(new, r1)

class test_load_from_file(unittest.TestCase):
    """ represent class that test load_from_fle()"""
    @classmethod
    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

    def test_with_nofile(self):
        load = Rectangle.load_from_file()
        self.assertEqual(load, "[]")
    
    def test_with_jfile(self):
        """ test with jsonfile"""
        lis_dic = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([lis_dic])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), len([lis_dic]))
