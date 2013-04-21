#!/usr/bin/env python2
 # -*- coding: utf-8 -*-

import sys
import select

import fileinput

sparks = ['▁','▂','▃','▄','▅','▆','▇','█']
def getSparks( numbers ):
	maximum = 0
	minimum = sys.maxint
	for n in numbers:
		if n > maximum:
			maximum = n
		if n < minimum:
			minimum = n


	div = float(maximum - minimum)
	output = ""

	for n in numbers:
		pos = int((n - minimum)/div * 7)
		output += sparks[pos]

	return output


def stringToNumerList( string ):
	numbers = []
	for n in numberString:
		try:
			numbers.append(float(n))
		except ValueError:
			pass
	return numbers


def help():
	return '''USAGE:
  spark.py VALUE [,] ...

EXAMPLES:
  spark.py 1 5 22 13 53
  ▁▁▃▂█
  spark.py 1.2 5.5 22.9 13.2 53.3
  ▁▁▃▂█
  sparkpy 0,30,55,80,33,150
  ▁▂▃▄▂.█
  echo 9 13 5 17 1 | spark.py
  ▄▆▂█▁'''


if __name__ == "__main__":

	def convertAndPrint( numberString ):
		numbers = stringToNumerList( numberString )
		if len(numbers) <= 2:
			print help()
		else:
			print getSparks( numbers )


	numberString = []
	for arg in sys.argv:
		numberString += arg.split(',')

	while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
		line = sys.stdin.readline()
		if line:
			numberString += line.split(' ')
		else:
			convertAndPrint( numberString )
			exit(0)
	else:
		pass

	convertAndPrint( numberString )