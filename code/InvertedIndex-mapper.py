#!/usr/bin/python

# Udacity MapReduce Lesson 4 - Inverted Index. Mapper function

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')

list = []
for line in reader :
    id = line[0]
    body = line[4]

    # Finding the count of the word 'fantastic' using regex
    words = re.findall(r"[\w']+", body)
    #for word in words :
	#if word.lower() == 'fantastic' :
	 #   print "{0}\t{1}".format(word, 1)

    # id is the node_id
    word = 'fantastically'
    if word in (w.lower() for w in words) :
	list.append([int(id), word])

list = sorted(list)

for it in list :
    print "{0}\t{1}".format(it[0], it[1])
