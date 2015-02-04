#!/usr/bin/python

import sys, argparse
from src.Steganana import Steganana


def main(argv):
	parser = argparse.ArgumentParser(description='Easy to use steganography tool')
	parser.add_argument('file', help='input file to be used to encode or decode the string')
	parser.add_argument('--encode', help='encode the given string in the file')
	parser.add_argument('--output', help='output file of the encoding process')
	args = parser.parse_args()

	steganana = Steganana(args.file)
	if(args.encode != ''):
		print steganna.decode()
	else:
		steganna.encode(args.output)

if __name__ == '__main__':
	main(sys.argv[1:])
