#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# spark.py-  https://github.com/jfreax/spark.py
# Print sparks like ▁▂▃▅▂▇ in your shell or use it in your python projects
#
# Copyright (C) 2013  Jens Dieskau
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License 2 as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
import sys
import select
import fileinput

sparks = ['▁','▂','▃','▄','▅','▆','▇','█']

def getSparks( numbers ):
	maximum = max(numbers)
	minimum = min(numbers)

	div = float(maximum - minimum)
	return ''.join( sparks[int((n - minimum)/div * 7)] for n in numbers)


def stringToNumberList( string ):
	numbers = []
	for n in string:
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
  spark.py 0,30,55,80,33,150
  ▁▂▃▄▂.█
  echo 9 13 5 17 1 | spark.py
  ▄▆▂█▁'''


if __name__ == "__main__":

	def convertAndPrint( numberString ):
		numbers = stringToNumberList( numberString )
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