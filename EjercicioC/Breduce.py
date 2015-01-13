#!/usr/bin/env python

import sys

value = 0.0
for line in sys.stdin:
	rec = line.strip(' \t\n\r').split()
	if len(rec) != 1:
		print 'Formato incorrecto'
		exit()

	try:
		value += float(rec[0])
	except ValueError:
		print 'Formato incorrecto'


print '%f' % (value)
