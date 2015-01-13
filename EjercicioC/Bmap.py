#!/usr/bin/env python

import sys

def function(v1, v2):
	return v1+v2;

def area(points):
	t1 = points[0]*points[3] + points[2]*points[5] + points[4]*points[1]
	t2 = points[1]*points[2] + points[3]*points[4] + points[5]*points[0]
	return (t1-t2)/2.0;

sum = 0.0
for line in sys.stdin:
	rec = line.strip(' \t\n\r').split()
	if len(rec) != 6:
		print 'Formato incorrecto'
		exit()

	try:
		rec[0] = float(rec[0])
		rec[1] = float(rec[1])
		rec[2] = float(rec[2])
		rec[3] = float(rec[3])
		rec[4] = float(rec[4])
		rec[5] = float(rec[5])
	except ValueError:
		print 'Formato incorrecto'
		exit()

	value = area(rec)/3.0
	value *= (function(rec[0], rec[1]) + function(rec[2], rec[3]) + function(rec[4], rec[5]))
	sum += value

print '%f' % (sum)
