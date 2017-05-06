#!/usr/bin/env python3
import math

class Point:
	'Represents a point in two-dimensional geometric coordinates'

	def __init__(self, x=0, y=0):
		'''Initialize the position of a new point.'''
		self.move(x, y)

	def move(self, x, y):
		"Move the point to a new location in two-dimensional space."
		self.x = x
		self.y = y

	def reset(self):
		'Reset the point back to the geometric origin: 0, 0'
		self.move(0, 0)

	def calculate_distance(self, other_point):
		"""Calculate the distance from this point to a second poitn passed as a parameter."""
		return math.sqrt(
			(self.x - other_point.x)**2 +
			(self.y - other_point.y)**2)

