#!/usr/bin/env python

import sys

dic = {}

def getVectorValue(index):
	return 1.0;

#(row column value)
for line in sys.stdin:
	rec = line.strip(' \t\n\r').split()
	if len(rec) != 3:
		print 'Formato incorrecto'
		exit()

	try:
		rec[0] = int(rec[0])   # row
		rec[1] = int(rec[1])   # column
		rec[2] = float(rec[2]) # value
	except ValueError:
		print 'Formato incorrecto'
		exit()
	
	if rec[0] in dic.keys():
		dic[rec[0]] += rec[2]*getVectorValue(rec[1])
	else:
		dic[rec[0]] = rec[2]*getVectorValue(rec[1])
	

keys = dic.keys()
keys.sort()

for w in keys:
	print '%d %f' % (w, dic[w])
