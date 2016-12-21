#!/usr/bin/python
import sys

max = 0
pathName = None
for line in sys.stdin :
	data = line.split("\t")
	path, count = data
	count = int(count)
	if max < count :
		#print pathName ,"\t", max
		max = count
		pathName = path

print pathName ,"\t", max

