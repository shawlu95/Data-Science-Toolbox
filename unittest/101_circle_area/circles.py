from math import pi

def circle_area(r):
	if r < 0:
		raise ValueError("value is negative")
	if type(r) not in [int, float]:
		raise TypeError("not integer or type")
	return pi * r ** 2