#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ class to test max_integer() """
    def test_max_integer(self):
        """ creates several assertions to test max_integer """
        var = max_integer([1, 2, 3, 4])
        some_list = [1, -3, 5, 3, -6]
        lenght = len(some_list)
        self.assertEqual(var, 4)
        self.assertIs(max_integer([7, 3, 4]), 7)
        self.assertIsNot(var, 3)
        self.assertNotEqual(var, 2)
        self.assertIsInstance(var, int)
        self.assertNotIsInstance(var, list)
        self.assertEqual(max_integer([2, 6, 1]), 6)
        self.assertTrue(lenght, 0)
        self.assertTrue(lenght, 1)
        self.assertIn(5, some_list)
        self.assertNotIn(2, some_list)
        self.assertNotIn('a', some_list)

        with self.assertRaises(TypeError):
            max_integer([None, True])
        with self.assertRaises(TypeError):
            max_integer(2)
        with self.assertRaises(TypeError):
            max_integer(True)
        with self.assertRaises(TypeError):
            max_integer(False)
        with self.assertRaises(KeyError):
            max_integer({'a': 1, 'b': 2, 'c': 3})
