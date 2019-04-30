# python3 -m unittest circles_test.py 
import unittest
from circles import circle_area
from math import pi

# give a descriptive class name
class TestCircleArea(unittest.TestCase):
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