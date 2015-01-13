#!/usr/bin/env python

import sys
import re

dic = {}

for line in sys.stdin:
#   words = line.strip(' \t\n\r').lower().split()
#   https://docs.python.org/2/library/re.html
    words = re.findall('\w+', line.lower())
    for w in words:
		if w in dic.keys():
			dic[w] += 1
		else:
			dic[w] = 1
keys = dic.keys()
keys.sort()

for w in keys:
	print '%s %d' % (w, dic[w])
	
