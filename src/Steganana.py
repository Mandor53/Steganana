# Steganana.py

import os, time
from PIL import Image

class Steganana:

	def __init__(self, file, silentmode):
		self.file       = file
		self.signature  = 'Stegananasignature'
		self.silentMode = silentmode

		self.info('Steganana instance launched')
		try:
			self.image = Image.open(file)
			self.image.load()
		except:
			self.error('Unabled to load the image')
			exit(2)

	def encode(self, text, isFile, output):
		self.info('Encoding...')

		content = ''

		if(isFile):
			with file(text) as f: content = f.read()
		else:
			content = text

		if(not self.checkAvailableStorage(self.signature + content)):
			self.error('This image is too small to store this data')
			return

		binaryString = self.getBinaryString(self.signature + content)

		for y in range(0, self.image.size[1]):
			for x in range(0, self.image.size[0]):
				r = self.image.getpixel((x, y))[0]
				g = self.image.getpixel((x, y))[1]
				b = self.image.getpixel((x, y))[2]
				a = self.image.getpixel((x, y))[3]
				i = 0
				while i < 3 and len(binaryString) > 0:
					if(i == 0):
						r = self.manageOddEven(r, binaryString[0])
					elif(i == 1):
						g = self.manageOddEven(r, binaryString[0])
					elif(i == 2):
						b = self.manageOddEven(r, binaryString[0])
					binaryString = binaryString[1:]
					i += 1
				self.image.putpixel((x, y), (r, g, b, a))

		self.image.save(output)
		self.info('Saved!')

	def decode(self):
		decoded = self.decodeRaw()

		if(self.signature != decoded[:len(self.signature)]):
			self.error('This file doesn\'t seem to contain any hidden text')
			return

		self.info('Decoded text:')
		return decoded[len(self.signature):]

	def decodeRaw(self):
		decoded = ''
		curChar = ''

		for y in range(0, self.image.size[1]):
			for x in range(0, self.image.size[0]):
				curColor = self.image.getpixel((x, y))
				curChar += str(int(curColor[0] % 2))
				curChar += str(int(curColor[1] % 2))
				curChar += str(int(curColor[2] % 2))

				if(curChar[:8] == '00000000'):
					return decoded
				if(len(curChar) >= 8):
					decoded += self.bin2char(curChar[:8])
					curChar = curChar[8:]

		return decoded

	def checkAvailableStorage(self, text):
		return self.image.size[0] * self.image.size[1] * 3 > \
			(len(text) + 1) * 8

	def getBinaryString(self, text):
		binaryString    = ''
		curTextPosition = 0

		while(curTextPosition < len(text)):
			curChar          = text[curTextPosition]
			curTextPosition += 1

			binaryString += self.char2bin(curChar)

		return binaryString + '00000000'

	def formatBin(self, i, clen):
		i = i.replace('0b', '')

		while len(i) < clen:
			i = '0' + i
		return i

	def char2bin(self, i):
		return self.formatBin(bin(ord(i)), 8)

	def bin2char(self, i):
		return chr(int(i, base=2))

	def makeOdd(self, number):
		return number | 1

	def makeEven(self, number):
		return number & ~1

	def manageOddEven(self, number, base):
		if(base == '0'):
			return self.makeEven(number)
		else:
			return self.makeOdd(number)

	def info(self, text):
		if(self.silentMode):
			return;
		print('    > ' + text)

	def error(self, text):
		print('  ## ' + text)
