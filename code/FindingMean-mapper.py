#!/usr/bin/python

# Udacity MapReduce Lesson 4 - Finding Mean. Mapper function

import sys
from datetime import datetime

for line in sys.stdin:
    line = line.split('\t')
    if len(line) < 6 :
	continue
    #print line[0]
    weekday = datetime.strptime(line[0], "%Y-%m-%d").weekday()
    sale = line[4]
    print "{0}\t{1}".format(weekday, sale)
