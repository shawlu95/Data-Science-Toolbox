# combine source code and test cases in a single file
# This can be directly run in coder pad

import unittest
from math import pi

def circle_area(r):
    if r < 0:
        raise ValueError("value is negative")
    if type(r) not in [int, float]:
        raise TypeError("not integer or type")
    return pi * r ** 2

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

# this line is optional
# if __name__ == '__main__':
#     unittest.main()

unittest.main()
