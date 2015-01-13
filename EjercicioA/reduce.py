#!/usr/bin/env python

import sys

dic = {}

for line in sys.stdin:
	rec = line.strip(' \t\n\r').split()
	if len(rec) != 2:
		continue

	try:
		rec[1] = int(rec[1])
	except ValueError:
		continue
	
	if rec[0] in dic.keys():
		dic[rec[0]] += rec[1]
	else:
		dic[rec[0]] = rec[1]

keys = dic.keys()
keys.sort()

for w in keys:
	print '%s %d' % (w, dic[w])
