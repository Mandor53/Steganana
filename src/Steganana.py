# Steganana.py

import os
from PIL import Image

class Steganana:

	def __init__(self, file):
		print("Steganana instance launched")
		self.file = file
		try:
			self.image = Image.open(file)
			self.image.load()
		except:
			print("Unable to load the image")
			exit(2)

	def encode(self, text, output):
		print("Encoding..")

		if(output == None):
			output = 'output.png'

		curTextPosition  = 0
		curImagePosition = 0

		while(curTextPosition < len(text)):
			curChar = text[curTextPosition]
			curTextPosition += 1

			print bin(ord(curChar))[2]

		print self.image.getpixel((0, 0))
