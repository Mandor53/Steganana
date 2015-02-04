# Steganana.py

from PIL import Image

class Steganana:

	def __init__(self, file):
		print("Steganana instance launched")
		self.file = file
		try:
			this.image = Image.open(file)
			this.image.load()
		except:
			print("Unable to load the image")
			return

	def encode(self, text, output):
		print("Encoding...")
