#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys
import csv

writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

keyA = None
keyB = None

for line in sys.stdin:
    #print line
    # YOUR CODE HERE
    lines = line.strip().split('\t')
    #print lines
    #print lines[0], lines[1],"A", lines[1] != "A"
    id = str(lines[1])
    
    if lines[1] == '"A"' :
	#print "TYPE A"
        keyA = lines[0]
	userData = lines[2:]
    elif lines[1] == '"B"' :
	#print "TYPE B"
        keyB = lines[0]
	nodeData = lines[2:]
	
    if keyA == keyB :
	#print keyA
	#print keyB
	writer.writerow(nodeData + [keyA] + userData)

