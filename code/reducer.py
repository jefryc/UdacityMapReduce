#!/usr/bin/python

# Instead of breaking the sales down by store, instead give us a sales breakdown by product category across all of our stores.

import sys

salesTotal = 0
currentMax = 0
oldKey = None
key = None
count = 0;
# It will be in the format key\tval
# Where key is the store name, val is the sale amount

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    #thisSale = float(thisSale)
    #salesTotal += thisSale
    #count += 1
    if oldKey and oldKey != thisKey:
        #print oldKey, "\t", salesTotal
        if currentMax < salesTotal:
    	    currentMax = salesTotal
    	    key = oldKey
    	oldKey = thisKey
        salesTotal = 0

    oldKey = thisKey
    salesTotal += int(thisSale)


#print key, "\t", currentMax
#print count, "\t", salesTotal
if oldKey != None:
    if (currentMax < salesTotal) :
	currentMax = salesTotal
	key = oldKey
    print key, "\t", currentMax 

