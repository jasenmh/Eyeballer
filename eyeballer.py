import numpy as np
import cv2

class eyeballer:
    # ---------- Private methods ----------
	def __init__(self):
		self.detect_targets = False
		self.last_image = None
		self.average_image = None
		self.target_bounds = None

	def _target_bounding_boxes(self):
		pass

    # ---------- Public methods ----------
	def add_image(self, image):
		""" 
		This method takes a new image, adds it to the average image, and
		applies all CV algorithms it is set to use. It then returns the 
		average image.
		:param image: next image to add to scene average
		:return: average image
		"""
		return self.average_image

