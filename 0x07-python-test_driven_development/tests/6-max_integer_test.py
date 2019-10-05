#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_string(self):
        self.assertAlmostEqual(max_integer("Hola"), "o")

    def test_max(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)

    def test_float(self):
        self.assertAlmostEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_float_neg(self):
        self.assertAlmostEqual(max_integer([-1.5, -2.5, -3.5, -4.5]), -1.5)

    def test_max_neg(self):
        self.assertAlmostEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_tuple(self):
        self.assertAlmostEqual(max_integer((1, 2, 6, 3)), 6)

    def test_empty(self):
        self.assertAlmostEqual(max_integer([]), None)

    def test_except(self):
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, [1, 2, "hi", 4])
        self.assertRaises(TypeError, max_integer, {1, 2, 6, 4})
        self.assertRaises(TypeError, max_integer, [1, 2, 6, 4], 5)
