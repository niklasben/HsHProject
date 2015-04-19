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


readfile = open("tweetfile.txt", "r")                                            #substitute tweetfile.txt with filename
read = open("tweetfile.txt", "r")       
#writefile = open("output.txt", "w")                                             #substitute output.txt with filename


## Tweetfile

#for line in readfile:
#    tweetfile_split = line.split()
#    tweetfile_split = len(tweetfile_split)
#    print "Zeile: " + str(tweetfile_split)

#line_nr_tweetfile = len(readfile.readlines())
#print "Tweetfile: " + str(line_nr_tweetfile)

#
## Neutrals
#read_neutral = open("germanneutral.tsv", "r")
##    for line in csv.reader(germanneutral.tsv, dialect="excel-tab")
#
#count_neutral = 0
#
#line_nr_neutral = len(read_neutral.readlines())
#print "Neutral: " + str(line_nr_neutral)
#
#for line in read_neutral:
#    token_neutral = line.strip().split('\t')
#    t_neutral = token_neutral[0]
#    #print t_neutral
#
#read_neutral.close()                                                            #closes opened file


# Positives
read_positive = open("germanpositive.tsv", "r")
read_pos = open("germanpositive.tsv", "r")
#    for line in csv.reader(germanpositive.tsv, dialect="excel-tab")

#count_positive = 0

line_nr_positive = len(read_positive.readlines())
#print "Positive: " + str(line_nr_positive)


for line in readfile:
    
    for line in readfile:
        tweetfile_split = line.split()
        tweetfile_split = len(tweetfile_split)
        
        for i in range(0, tweetfile_split):
            token_tweet = line.strip().split('\t')
            t_tweet = token_tweet[i]
            t_tweet = t_tweet.lower()
            
            for line in read_pos:
                token_positive = line.strip().split('\t')
                t_positive = token_positive[0]
                t_positive = t_positive.lower()
                
                if t_tweet == t_positive:
                    print 'true'
                else:
                    print 'false'
                
                #print t_positive            
            
            #print token_tweet[i]



#for line in read_pos:
#    token_positive = line.strip().split('\t')
#    t_positive = token_positive[0]
#    t_positive = t_positive.lower()
#    #print t_positive
#    
#    for j in range(0, len(tweetfile_split)):
#        for line in read:
#            token_tweet = line.strip().split('\t')
#            t_tweet = token_tweet[j]
#            t_tweet = t_tweet.lower()
#            
#            c = 1
#            for i in range(0, line_nr_positive):
#                print str(c)
#                c = c+1
#                #if t_positive == word

read_positive.close()                                                           #closes opened file
read_pos.close()                                                                #closes opened file


## Negatives
#read_negative = open("germannegative.tsv", "r")
##    for line in csv.reader(germannegative.tsv, dialect="excel-tab")
#
#count_negative = 0
#
#line_nr_negative = len(read_negative.readlines())
#print "Negative: " + str(line_nr_negative)
#
#for line in read_negative:
#    token_negative = line.strip().split('\t')
#    t_negative = token_negative[0]
#    #print t_negative
#
#read_negative.close()                                                           #closes opened file

# Writing into Tweetfile
#for line in readfile:
#    writefile.write(str(line.replace('\n', '')) + "\t\t\tneutral: " + str(count_neutral) + "\tpositiv: " 
#    + str(count_positive) + "\tnegativ: " + str(count_negative) + "\n")


#for line in readfile:
#    print line ## From this print you can see if 'line' variable has each line from the file. 
               #And also the structure of each line. This print is just for test, put it in comment.
               #The words in the line have separated by \t.
#    token = line.strip().split('\t')  ## To split the words by tab and access them one by one
#    print token[0] ## This print shows you the first word from the line.
    ### The token variable has all the words separately from the line. You can access them by their index.
    
#    writefile.write(str(line.replace('\n', '')) + "\t\t\tneutral: " + "\tpositiv: " + "\tnegativ: \n")
    #### Instead of replacing '\n' (line.replace('\n', '')). You can use line.strip(), and '\n' will be gone.


readfile.close()                                                                #closes opened file
#writefile.close()                                                               #closes opened file
