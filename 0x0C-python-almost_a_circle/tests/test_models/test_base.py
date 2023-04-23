#!/usr/bin/python3
""" This module contains unittest cases for base.py """
import unittest
Base = __import__("base").Base


class TestBase(unittest.TestCase):
    """ creates a test class for the base.py file """
    def test_initial_value(self):
        """ tests the init constructor """
        obj_1 = Base()
        self.assertEqual(obj_1.id, 1)
        self.assertIsNotNone(obj_1.id)
        self.assertNotEqual(obj_1.id, 0)
        
        obj_2 = Base(12)
        self.assertNotEqual(obj_2.id, 1)
        self.assertEqual(obj_2.id, 12)
        self.assertIsNotNone(obj_2.id)

        obj_3 = Base()
        self.assertEqual(obj_3.id, 2)
        self.assertIsNotNone(obj_3.id)
        self.assertNotEqual(obj_3.id, 1)
