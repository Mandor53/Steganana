#!/usr/bin/python

import sys, argparse
from src.Steganana import Steganana


def main(argv):
	parser = argparse.ArgumentParser(description='Easy to use steganography tool')
	parser.add_argument('file', help='input file to be used to encode or decode the string')
	parser.add_argument('--encode', help='encode the given string/file into the image')
	parser.add_argument('--encode-file', help='encode from the given file (from --encode)', dest='fromfile', action='store_true')
	parser.add_argument('--encode-string', help='encode using the given string (from --encode)', dest='fromfile', action='store_false')
	parser.add_argument('--output', help='output file of the encoding process', nargs='?')
	parser.add_argument('--silent', help='silent mode, does not output anything except decoded data', dest='silent', action='store_true')
	parser.add_argument('--verbose', help='verbose mode, outputs what\'s going on under the hood', dest='silent', action='store_false')
	parser.set_defaults(silent=False, fromfile=False, output='output.png')
	args = parser.parse_args()

	steganana = Steganana(args.file, args.silent)
	if(args.encode == None):
		print steganana.decode()
	else:
		steganana.encode(args.encode, args.fromfile, args.output)

if __name__ == '__main__':
	main(sys.argv[1:])
