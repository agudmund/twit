#!/usr/bin/env python

import sys
import random
import twits

class Jumble:
	def __init__(self, sentence):
		self.name = 'Word scramble'
		self.sentence = sentence.split( ' ' )

	def swap(self, a,b,):
		"""Swaps the index of two given items in a list"""

		result = self.sentence

		location_a = result.index(a)
		location_b = result.index(b)
		
		result.remove(a)
		result.insert(location_b,a)
		result.remove(b)
		result.insert(location_a,b)

		return result
	
if __name__ == '__main__':

	# Tested using 5 random sentences generated from online language study: http://www.manythings.org/rs/presentcontinuous.html
	sentences = [
	'Those gardeners are jogging in the mountains',
	'That musician is not surfing at the bank',
	'Is the plumber sleeping near our school',
	"I'm not eating near our school",
	"Rosie isn't fighting nowadays",
	]

	twit = twits.Twitterings()
	sentences = [n.text for n in twit.public()]
	print(sentences)

	for sentence in sentences:
		print('\n--[ Test case: "%s"' % sentence)
		scramble = Jumble( sentence )

		x= random.choice(scramble.sentence)
		y= random.choice(scramble.sentence)

		while x==y:
			y= random.choice(scramble.sentence)			

		print ('\t--[ Swapping "%s" for "%s"' % (x,y))
		print (scramble.swap(x,y))

