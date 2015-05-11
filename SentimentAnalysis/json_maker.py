# -*- coding: utf-8 -*-
"""
Created on Tue May 05 09:45:42 2015

@author: Niklas Bendixen
"""

from collections import OrderedDict
import json
 

### Operations for neutral opinion
#read_neutral = open("GermanPolarityClues-Neutral-umlaute.tsv", "r")             # Open file with neutral words
#neu = {}                                                                        # Building neutral dictionary
#for n in read_neutral:                                                          # Adding words to neutral dictionary
#    n = n.strip().split('\t')
#    neu[n[0]] = n[len(n)-1]
#
#### Operations for positive opinions
#read_positive = open("GermanPolarityClues-Positive-umlaute.tsv", "r")           # Open file with positive words
#pos = {}                                                                        # Building positive dictionary
#for p in read_positive:                                                         # Adding words to positive dictionary
#    p = p.strip().split('\t')
#    pos[p[0]] = p[len(p)-1]
#
#### Operations for negative opinions
#read_negative = open("GermanPolarityClues-Negative-umlaute.tsv", "r")           # Open file with negative words
#neg = {}                                                                        # Building negative dictionary
#for ne in read_negative:                                                        # Adding words to negative dictionary
#    ne = ne.strip().split('\t')
#    neg[ne[0]] = ne[len(ne)-1]
#
#### Tweetfile
#readfile = open("testjson.txt", "r")                                           # File with the labeled data
#writefile = open("tweets.txt", "w")                                             # File for the ouput
#
#for line in readfile:                                                           # Looping through every line of readfile
#    token_tweet = line.strip().split('\t')                                      # Tokenize each line by tab-seperated words
#    tweetfile_split = line.split()
#    tweetfile_split = len(tweetfile_split)                                      # Counting number of words in line
#    count_neutral = 0                                                           # Reset count_neutral to zero
#    count_positive = 0                                                          # Reset count_positive to zero
#    count_negative = 0                                                          # Reset count_negative to zero
#    for i in range(2,len(token_tweet)):                                         # looping through each word of a line        
#        #t_tweet = token_tweet[i]                                               # For Testing Purposes Only
#        #print t_tweet                                                          # For Testing Purposes Only
#        if token_tweet[i] in neu.keys():
#            opinion_neu = neu[token_tweet[i]]                                   # This way you can get the opinion of token 'i' if neutral
#            count_neutral = count_neutral + 1
#            #print "neutral " + str(count_neutral)                              # For TestingPurposes Only
#        elif token_tweet[i] in pos.keys():
#            opinion_pos = pos[token_tweet[i]]                                   # This way you can get the opinion of token 'i' if positive
#            count_positive = count_positive + 1
#            #print "positive " + str(count_positive)                            # For Testing Purposes Only
#        elif token_tweet[i] in neg.keys():
#            opinion_neg = neg[token_tweet[i]]                                   # This way you can get the opinion of token 'i' if negative
#            count_negative = count_negative + 1
#            #print "negative " + str(count_negative)                            # For Testing Purposes Only    
#    if count_negative > count_positive:                                         # If the number of negative tokens is bigger than positive
#        writefile.write('-\t' + line)                                           # Label the line as negative
#    elif count_negative < count_positive:                                       # If the number of negative tokens is smaller than positive
#        writefile.write('+\t' + line)                                           # Label the line as positive
#    elif count_negative == count_positive:                                      # If the number of negative and positive tokens is equal
#        writefile.write('0\t' + line)                                           # Label the line as neutral
#    elif count_negative == 0 and count_positive == 0:                           # If the number of negative and positive tokens is zero in total
#        writefile.write('undef\t' + line)                                       # Label the line as neutral
#readfile.close()                                                                # Closes opened file readfile
#read_neutral.close()                                                            # Closes opened file read_neutral
#read_positive.close()                                                           # Closes opened file read_positive
#read_negative.close()                                                           # Closes opened file read_negative
#writefile.close()                                                               # Closes opened file writefile





# Open the workbook and select the first worksheet
read = open("tweets.txt", "r")

countries = []
topics = []

for line in read:
    line = line.strip().replace("\xc3\xbc", "ue").replace("\xc3\xa4", "ae").split('\t')
    if line[2] not in countries:
        countries.append(line[2])
    if line[1] not in topics:
        topics.append(line[1])

#print countries
#print topics

### Dictionaries
dict_all = {}
dict_pos = {}
dict_neg = {}

for i in countries:
    dict_all[i] = [0]*len(topics)
    dict_pos[i] = [0]*len(topics)
    dict_neg[i] = [0]*len(topics)

#print dict_all
#print dict_pos
#print dict_neg

for line in read:
    line = line.strip().
    


















 
## List to hold dictionaries
#list = []
#
# 
# 
## Iterate through each row in worksheet and fetch values into dict
#for rownum in range(1, sh.nrows):
#    cars = OrderedDict()
#    row_values = sh.row_values(rownum)
#    cars['OEM-Brand'] = row_values[0]
#    cars['make'] = row_values[1]
#    cars['model'] = row_values[2]
#    cars['miles'] = row_values[3]
# 
#    list.append(cars)
# 
## Serialize the list of dicts to JSON
#j = json.dumps(list)
# 
## Write to file
#with open('data.json', 'w') as f:
#    f.write(j)
#
#read.close()
#f.close()