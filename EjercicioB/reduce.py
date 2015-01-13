#!/usr/bin/env python

import sys

dic = {}

for line in sys.stdin:
	rec = line.strip(' \t\n\r').split()
	if len(rec) != 2:
		print 'Formato incorrecto'
		exit()

	try:
		rec[0] = int(rec[0])   # row
		rec[1] = float(rec[1]) # value
	except ValueError:
		print 'Formato incorrecto'
		exit()
	
	if rec[0] in dic.keys():
		dic[rec[0]] += rec[1]
	else:
		dic[rec[0]] = rec[1]

keys = dic.keys()
keys.sort()

for w in keys:
	print '%d %f' % (w, dic[w])
