# python3 -m unittest circles_test.py
import unittest
from circles import circle_area
from math import pi

# give a descriptive class name
class TestCircleArea(unittest.TestCase):
	"""
	Assertion methods:

	assertEqual(a, b)
	assertAlmostEqual(a, b)
	assertNotEqual(a, b)
	assertTrue(x)
	assertFalse(x)
	assertIs(a, b)
	assertIsNot(a, b)

	assertIsNone(x)
	assertIsNotNone(x)

	assertIn(a, b)
	assertNotIn(a, b)

	assertIsInstance(a, b)
	assertNotIsInstance(a, b)

	assertRaises()
	assertRaisesRegexp()
	"""
	def test_area(self):
		# almost equal: must match 7 decimal places
		self.assertAlmostEqual(circle_area(1), pi)
		self.assertAlmostEqual(circle_area(0), 0)
		self.assertAlmostEqual(circle_area(2.1), pi * 2.1 ** 2)

	def test_values(self):
		self.assertRaises(ValueError, circle_area, -2)

	def test_types(self):
		self.assertRaises(TypeError, circle_area, 3 + 5j)
		self.assertRaises(TypeError, circle_area, True)
		self.assertRaises(TypeError, circle_area, "0")
