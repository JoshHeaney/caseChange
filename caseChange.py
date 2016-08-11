#!/usr/bin/python
#Reformat the input string

import sys
import string
import binascii
from optparse import OptionParser

#Optional arguments
parser = OptionParser("python caseChange.py [option(s)] [string(s)]\n Convert the input strings to the specified case.\n Use quotation marks(\") around phrases.")
parser.add_option("-u", "--uppercase", action="store_true", dest="upper", default=False, help="input converted to all caps")
parser.add_option("-l", "--lowercase", action="store_true", dest="lower", default=False, help="input converted to all lower")
parser.add_option("-t", "--titlecase", action="store_true", dest="title", default=False, help="input converted to title case")
parser.add_option("-e", "--eachword", action="store_true", dest="each", default=False, help="capitalize each word in input")
parser.add_option("-i", "--invert", action="store_true", dest="invert", default=False, help="invert case of input")
(options, args) = parser.parse_args()


if len(args) >= 1:
	for input in args:
		input = str(input)
		if options.upper:
			print (str(input).upper())
		if options.lower:
			print (str(input).lower())
		if options.title:
			# Lower in title:
			# Articles: a, an, & the.
			# Coordinate conjunctions: for, and, nor, but, or, yet, so 
			# Prepositions: at, around, by, after, along, for, from, of, on, to, with, without.
			# Capitalized in a title:
			# The first and last words, always.
			# All nouns, pronouns, adjectives, verbs and adverbs should be capitalized.
			# Subordinate conjunctions: after, as, because, how, who, if, than, what, why, that, when, where, whether, while.
			# Commonly missed words: it (pronoun), is (verb), and their/our/my (adjective) should all be capitalized.
			uncaps = ['as', 'be', 'a', 'an', 'the', 'for', 'and', 'nor', 'but', 'or', 'yet', 'so', 'at', 'around', 'by', 'after', 'along', 'for', 'from', 'of', 'on', 'to', 'with', 'without']
			parts = input.split(' ')
			input =''
			for word in parts:
				input += word.capitalize() + ' '
			parts = input.split(' ')
			
			max = len(parts)-2
			if max > 0:
				sys.stdout.write(parts[0] + ' ')
			for i in range(1,max):
				if parts[i].lower() in uncaps:
					sys.stdout.write(parts[i].lower() + ' ')
				else:
					sys.stdout.write(parts[i] + ' ')
			sys.stdout.write(str(parts[max]).capitalize() + '\n')
		if options.each:
			parts = input.split(' ')
			for word in parts:
				sys.stdout.write(word.capitalize() + ' ')
			sys.stdout.write('\n')
		if options.invert:
			for c in input:
				if str(c).isupper():
					sys.stdout.write(str(c).lower())
				elif str(c).islower():
					sys.stdout.write(str(c).upper())
				else:
					sys.stdout.write(c)
			sys.stdout.write('\n')
else:
	print("No string input!")
	sys.exit()