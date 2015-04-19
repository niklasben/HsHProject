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
import math
from itertools import repeat


# Neutrals                                                                      #Operations for neutral opinions
read_neutral = open("germanneutral.tsv", "r")

neu = {}

for n in read_neutral:
    n = n.strip().split('\t')
    neu[n[0]] = n[len(n)-1]


# Positives                                                                     #Operations for positive opinions
read_positive = open("germanpositive.tsv", "r")

pos = {}

for p in read_positive:
    p = p.strip().split('\t')
    pos[p[0]] = p[len(p)-1]


# Negatives                                                                     #Operations for negative opinions
read_negative = open("germannegative.tsv", "r")

neg = {}

for ne in read_negative:
    ne = ne.strip().split('\t')
    neg[ne[0]] = ne[len(ne)-1]
    

# Tweetfile                                                                     #It's getting serious
readfile = open("tweetfile.txt", "r")                                           #substitute tweetfile.txt with filename
#writefile = open("output.txt", "w")                                             #substitute output.txt with filename

for line in readfile:
    token_tweet = line.strip().split('\t')
    tweetfile_split = line.split()
    tweetfile_split = len(tweetfile_split)
    count_neutral = 0
    count_positive = 0
    count_negative = 0
    for i in range(0,len(token_tweet)):                                         # looping throw each words of a line        
        #t_tweet = token_tweet[i]
        if token_tweet[i] in neu.keys():
            opinion_neu = neu[token_tweet[i]]                                   # this way you can get the opinion of word 'i' token
            count_neutral = count_neutral + 1
            #print "neutral " + str(count_neutral)                              #For Testing
        elif token_tweet[i] in pos.keys():
            opinion_pos = pos[token_tweet[i]]                                   # this way you can get the opinion of word 'i' token
            count_positive = count_positive + 1
            #print "positive " + str(count_positive)                            #For Testing
        elif token_tweet[i] in neg.keys():
            opinion_neg = neg[token_tweet[i]]                                   # this way you can get the opinion of word 'i' token
            count_negative = count_negative + 1
            #print "negative " + str(count_negative)                            #For Testing
            print line + " - neutrals: " + str(count_neutral) + " | positives: " + str(count_positive) + " | negatives: " + str(count_negative)


### END OF LINE
read_neutral.close()                                                            #closes opened file
read_positive.close()                                                           #closes opened file
read_negative.close()                                                           #closes opened file
readfile.close()                                                                #closes opened file
#writefile.close(                                                               #closes opened file
