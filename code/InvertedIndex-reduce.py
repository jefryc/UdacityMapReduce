#!/usr/bin/python

# Udacity MapReduce Lesson 4 - Inverted Index. Reduce function

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

countWord = 0
word = None
list = []
for line in reader :
    if len(line) != 2 :
	continue
    # 1
    #if word == None :
    #	word = line[0]
    #countWord += int(line[1])

#print "{0}\t{1}".format(word, countWord)

    id = int(line[0])
    if word == None :
	word = line[1]
    list.append(id)

list = sorted(list)

print word, ":"
for id in list :
    print id,
