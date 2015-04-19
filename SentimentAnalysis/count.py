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
from itertools import repeat


readfile = open("tweetfile.txt", "r")                                           #substitute tweetfile.txt with filename
writefile = open("output.txt", "w")                                             #substitute output.txt with filename

read_neutral = open("germanneutral.tsv", "r")
#    for line in csv.reader(germanneutral.tsv, dialect="excel-tab")

read_positive = open("germanpositive.tsv", "r")
#    for line in csv.reader(germanpositive.tsv, dialect="excel-tab")

read_negative = open("germannegative.tsv", "r")
#    for line in csv.reader(germannegative.tsv, dialect="excel-tab")


# Neutrals

#count_neutral = 0

for line in read_neutral:
    token_neutral = line.strip().split('\t')
    t_neutral = token_neutral[0]
    print t_neutral


# Positives
#count_positive = 0

for line in read_positive:
    token_positive = line.strip().split('\t')
    t_positive = token_positive[0]
    print t_positive


# Negatives

#count_negative = 0

for line in read_negative:
    token_negative = line.strip().split('\t')
    t_negative = token_negative[0]
    print t_negative

#for line in readfile:
#    writefile.write(str(line.replace('\n', '')) + "\t\t\tneutral: " + "\tpositiv: " + "\tnegativ: \n")


#for line in readfile:
#    print line ## From this print you can see if 'line' variable has each line from the file. 
               #And also the structure of each line. This print is just for test, put it in comment.
               #The words in the line have separated by \t.
#    token = line.strip().split('\t')  ## To split the words by tab and access them one by one
#    print token[0] ## This print shows you the first word from the line.
    ### The token variable has all the words separately from the line. You can access them by their index.
    
#    writefile.write(str(line.replace('\n', '')) + "\t\t\tneutral: " + "\tpositiv: " + "\tnegativ: \n")
    #### Instead of replacing '\n' (line.replace('\n', '')). You can use line.strip(), and '\n' will be gone.


read_neutral.close()                                                            #closes opened file
read_positive.close()                                                           #closes opened file
read_negative.close()                                                           #closes opened file
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


#with open('germanneutral.tsv', 'rb') as tsvin, open('neutral.csv', 'wb') as csvout:
#    tsvin = csv.reader(tsvin, delimiter='\t')
#    csvout = csv.writer(csvout)
    
#    for row in tsvin:
#        count = int(row[0])
#        if count > 0:
#            csvout.writerows(repeat(row[0], 1))


#rneutral = r"germanneutral.tsv"
#csvfile = r"csv.csv"

#neu = csv.reader(open(rneutral, "rb"), delimiter = '\t')
#outcsv = csv.writer(open(csvfile, 'wb'))
#outcsv.writerows(neu)
