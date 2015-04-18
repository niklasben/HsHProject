# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:19:53 2015

@author: Niklas Bendixen
"""

import re                                                                       #import of regex
import codecs                                                                   #import of utf8 support
import csv                                                                      #import of csv
import sys
import glob
import string
import os

#read_neutral = open("germanneutral.tsv", "r")
#    for line in csv.reader(germanneutral.tsv, dialect="excel-tab")

#read_positive = open("germanpositive.tsv", "r")
#    for line in csv.reader(germanpositive.tsv, dialect="excel-tab")

#read_negative = open("germannegative.tsv", "r")
#    for line in csv.reader(germannegative.tsv, dialect="excel-tab")

readfile = open("tweetfile.txt", "r")                                           #substitute tweetfile.txt with filename
writefile = open("output.txt", "w")                                             #substitute output.txt with filename

#count_neutral = 0
#count_positive = 0
#count_negative = 0

#for line in readfile:
#    writefile.write(str(line.replace('\n', '')) + "\t\t\tneutral: " + "\tpositiv: " + "\tnegativ: \n")




#read_neutral.close()                                                           #closes opened file
#read_positive.close()                                                          #closes opened file
#read_negative.close()                                                          #closes opened file
readfile.close()                                                                #closes opened file
writefile.close()                                                               #closes opened file




### Tried and worthless ###

#n = re.search(r"^[\w]+[\s|\t]", readfile, re.multiline)
#m = re.match(r"^A-Za-z", line)
#for line in readfile:
#    writefile.write(str(line.replace('\n', '')) + "\t\t\t" + n)
    
    
#for line in sys.stdin.readlines():
#for line in readfile.readlines():
#    if line[0] == 'werde':
#        print line,
    
    
#for l in readfile.splitlines():
#    if re.search(r"^\w*[\t|\s]", l):
#        writefile.write(str(line.replace('\n', '')) + l + \n")    


#for line in readfile:
#    d = re.match("werde", line),
#if d:
#    print "true"
#else print "fail"
