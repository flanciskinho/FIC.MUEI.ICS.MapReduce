#!/usr/bin/env python

import sys

def function(value):
	return value*value;

sum = 0.0
for line in sys.stdin:
	rec = line.strip(' \t\n\r').split()
	if len(rec) != 2:
		print 'Formato incorrecto'
		exit()

	try:
		rec[0] = float(rec[0])
		rec[1] = float(rec[1])
	except ValueError:
		print 'Formato incorrecto'
		exit()

	value = (rec[1] - rec[0])/2.0
	value *= (function(rec[0]) + function(rec[1]))
	sum += value

print '%f' % (sum)
	
