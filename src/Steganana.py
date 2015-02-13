# Steganana.py

import os, time
from PIL import Image

class Steganana:

	def __init__(self, file, silentmode):
		# Storing our variables into the class's attribtues
		self.file       = file
		self.signature  = 'Stegananasignature'
		self.silentMode = silentmode

		self.info('Steganana instance launched')

		# Trying to open the image, and storing it
		try:
			self.image = Image.open(file)
			self.image.load()
		except:
			self.error('Unabled to load the image')
			exit(2)

	def encode(self, text, isFile, output):
		self.info('Encoding...')

		content = ''

		# Getting the content to encode
		if(isFile):
			with file(text) as f: content = f.read()
		else:
			content = text

		# Check if the image has enough space
		if(not self.checkAvailableStorage(self.signature + content)):
			self.error('This image is too small to store this data')
			return

		# Getting the binary equivalent of the content
		binaryString = self.getBinaryString(self.signature + content)

		# Looping through the pixels of the image
		for y in range(0, self.image.size[1]):
			for x in range(0, self.image.size[0]):
				# Getting all the components of the pixel
				r = self.image.getpixel((x, y))[0]
				g = self.image.getpixel((x, y))[1]
				b = self.image.getpixel((x, y))[2]
				a = self.image.getpixel((x, y))[3]
				i = 0

				# Looping through the image's components
				while i < 3 and len(binaryString) > 0:
					if(i == 0):
						r = self.manageOddEven(r, binaryString[0])
					elif(i == 1):
						g = self.manageOddEven(r, binaryString[0])
					elif(i == 2):
						b = self.manageOddEven(r, binaryString[0])
					binaryString = binaryString[1:]
					i += 1

				# Storing the new pixel
				self.image.putpixel((x, y), (r, g, b, a))

		# Saving the image
		self.image.save(output)
		self.info('Saved!')

	def decode(self):
		# Decode the content in the image, if any
		decoded = self.decodeRaw()

		# Checking if the image contains any content, using our signature
		if(self.signature != decoded[:len(self.signature)]):
			self.error('This file doesn\'t seem to contain any hidden text')
			return

		self.info('Decoded text:')
		return decoded[len(self.signature):]

	def decodeRaw(self):
		decoded = ''
		curChar = ''

		# Looping through the pixels
		for y in range(0, self.image.size[1]):
			for x in range(0, self.image.size[0]):
				# Getting the components of the pixel
				curColor = self.image.getpixel((x, y))
				curChar += str(int(curColor[0] % 2))
				curChar += str(int(curColor[1] % 2))
				curChar += str(int(curColor[2] % 2))

				# Checking if we've arrived to the end byte
				if(curChar[:8] == '00000000'):
					return decoded

				# Checking if we've decoded a whole byte
				if(len(curChar) >= 8):
					decoded += self.bin2char(curChar[:8])
					curChar = curChar[8:]

		# Returning the decoded content
		return decoded

	def checkAvailableStorage(self, text):
		# Checks if the number of pixels is enough to store the text
		return self.image.size[0] * self.image.size[1] * 3 > \
			(len(text) + 1) * 8

	def getBinaryString(self, text):
		binaryString    = ''
		curTextPosition = 0

		# Convert a string into a binary sequence
		while(curTextPosition < len(text)):
			curChar          = text[curTextPosition]
			curTextPosition += 1

			binaryString += self.char2bin(curChar)

		# Return the binary sequence, adding the null terminator
		return binaryString + '00000000'

	def formatBin(self, i, clen):
		# The default python byte formating is a bit weird, so fixing it
		i = i.replace('0b', '')

		# Adding the needed bits
		while len(i) < clen:
			i = '0' + i
		return i

	def char2bin(self, i):
		# Getting the binary equivalent of a char
		return self.formatBin(bin(ord(i)), 8)

	def bin2char(self, i):
		# Getting the char from a byte
		return chr(int(i, base=2))

	def makeOdd(self, number):
		# Make a number odd using bitwise operators
		return number | 1

	def makeEven(self, number):
		# Make a number even using bitwise operators
		return number & ~1

	def manageOddEven(self, number, base):
		# Needed by the project, makes a number even or odd depending
		# on the base
		return self.makeEven(number) if (base == '0') else self.makeOdd(number);

	def info(self, text):
		# Simply outputs some info message
		if(self.silentMode):
			return;
		print('    > ' + text)

	def error(self, text):
		# Simplfy outputs some error message
		print('  ## ' + text)
