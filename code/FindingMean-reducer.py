#!/usr/bin/python

# Udacity MapReduce Lesson 4 - Finding Mean. Reducer function
import sys

salesTotal = 0
oldKey = None
count=0

# Loop around the data
# It will be in the format key\tval
# Where key is the product name, val is the sale amount
#
# All the sales for a particular product  will be presented,
# then the key will change and we'll be dealing with the next product

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", float(salesTotal/count)
        oldKey = thisKey;
        salesTotal = 0
        count=0

    oldKey = thisKey
    salesTotal += float(thisSale)
    count+=1

if oldKey != None:
    print oldKey, "\t", float(salesTotal/count)
