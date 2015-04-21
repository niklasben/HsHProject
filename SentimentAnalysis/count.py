# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:19:53 2015

@author: Niklas Bendixen
"""

import re                                                                       # import of regex
import codecs                                                                   # import of utf8 support
import csv                                                                      # import of csv
import sys
import glob
import fileinput
import string
import os
import math
from itertools import repeat


# Neutrals                                                                      # Operations for neutral opinions
read_neutral = open("GermanPolarityClues-Neutral-Lemma-21042012.tsv", "r")      # Open file with neutral lemmas

neu = {}                                                                        # Building neutral dictionary

for n in read_neutral:                                                          # Adding words to neutral dictionary
    n = n.strip().split('\t')
    neu[n[0]] = n[len(n)-1]


# Positives                                                                     # Operations for positive opinions
read_positive = open("GermanPolarityClues-Positive-Lemma-21042012.tsv", "r")    # Open file with positive lemmas

pos = {}                                                                        # Building positive dictionary

for p in read_positive:                                                         # Adding words to positive dictionary
    p = p.strip().split('\t')
    pos[p[0]] = p[len(p)-1]


# Negatives                                                                     # Operations for negative opinions
read_negative = open("GermanPolarityClues-Negative-Lemma-21042012.tsv", "r")    # Open file with negative lemmas

neg = {}                                                                        # Building negative dictionary

for ne in read_negative:                                                        # Adding words to negative dictionary
    ne = ne.strip().split('\t')
    neg[ne[0]] = ne[len(ne)-1]
    

# Tweetfile                                                                     # It's getting serious
readfile = open("tweetfile.txt", "r")                                           # Substitute tweetfile.txt with filename
writefile = open("output.txt", "w")                                             # Substitute output.txt with filename

for line in readfile:                                                           # Looping through every line of the tweetfile
    token_tweet = line.strip().split('\t')                                      # Tokenize each line by tab-seperated words
    tweetfile_split = line.split()
    tweetfile_split = len(tweetfile_split)                                      # Counting number of words in line
    count_neutral = 0                                                           # Reset count_neutral to zero
    count_positive = 0                                                          # Reset count_positive to zero
    count_negative = 0                                                          # Reset count_negative to zero
    for i in range(0,len(token_tweet)):                                         # looping through each word of a line        
        #t_tweet = token_tweet[i]                                               # For Testing
        if token_tweet[i] in neu.keys():
            opinion_neu = neu[token_tweet[i]]                                   # this way you can get the opinion of word 'i' token
            count_neutral = count_neutral + 1
            #print "neutral " + str(count_neutral)                              # For Testing
        elif token_tweet[i] in pos.keys():
            opinion_pos = pos[token_tweet[i]]                                   # this way you can get the opinion of word 'i' token
            count_positive = count_positive + 1
            #print "positive " + str(count_positive)                            # For Testing
        elif token_tweet[i] in neg.keys():
            opinion_neg = neg[token_tweet[i]]                                   # this way you can get the opinion of word 'i' token
            count_negative = count_negative + 1
            #print "negative " + str(count_negative)                            # For Testing
    #print line + " - neutrals: " + str(count_neutral) + " | positives: " + str(count_positive) + " | negatives: " + str(count_negative)
    writefile.write(str(line.replace('\n', '')) + "\t | neutral: " + str(count_neutral) + "\t | positiv: " + str(count_positive) + "\t | negativ: " + str(count_negative) + "\n")

### END OF LINE
read_neutral.close()                                                            # Closes opened file
read_positive.close()                                                           # Closes opened file
read_negative.close()                                                           # Closes opened file
readfile.close()                                                                # Closes opened file
writefile.close()                                                               # Closes opened file