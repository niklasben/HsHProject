# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:19:53 2015

@author: Niklas Bendixen
"""

### Operations for neutral opinion
read_neutral = open("GermanPolarityClues-Neutral-umlaute.tsv", "r")             # Open file with neutral words
neu = {}                                                                        # Building neutral dictionary
for n in read_neutral:                                                          # Adding words to neutral dictionary
    n = n.strip().split('\t')
    neu[n[0]] = n[len(n)-1]

### Operations for positive opinions
read_positive = open("GermanPolarityClues-Positive-umlaute.tsv", "r")           # Open file with positive words
pos = {}                                                                        # Building positive dictionary
for p in read_positive:                                                         # Adding words to positive dictionary
    p = p.strip().split('\t')
    pos[p[0]] = p[len(p)-1]

### Operations for negative opinions
read_negative = open("GermanPolarityClues-Negative-umlaute.tsv", "r")           # Open file with negative words
neg = {}                                                                        # Building negative dictionary
for ne in read_negative:                                                        # Adding words to negative dictionary
    ne = ne.strip().split('\t')
    neg[ne[0]] = ne[len(ne)-1]

### Tweetfile
readfile = open\
("../labeling/dataset_labeled/theultimatefinalhyperdatasorted.txt", "r")        # File with the labeled data
writefile = open("sentiment_analysed_tweets.txt", "w")                          # File for the ouput

for line in readfile:                                                           # Looping through every line of readfile
    token_tweet = line.strip().split('\t')                                      # Tokenize each line by tab-seperated words
    tweetfile_split = line.split()
    tweetfile_split = len(tweetfile_split)                                      # Counting number of words in line
    count_neutral = 0                                                           # Reset count_neutral to zero
    count_positive = 0                                                          # Reset count_positive to zero
    count_negative = 0                                                          # Reset count_negative to zero
    for i in range(2,len(token_tweet)):                                         # looping through each word of a line        
        #t_tweet = token_tweet[i]                                               # For Testing Purposes Only
        #print t_tweet                                                          # For Testing Purposes Only
        if token_tweet[i] in neu.keys():
            opinion_neu = neu[token_tweet[i]]                                   # This way you can get the opinion of token 'i' if neutral
            count_neutral = count_neutral + 1
            #print "neutral " + str(count_neutral)                              # For TestingPurposes Only
        elif token_tweet[i] in pos.keys():
            opinion_pos = pos[token_tweet[i]]                                   # This way you can get the opinion of token 'i' if positive
            count_positive = count_positive + 1
            #print "positive " + str(count_positive)                            # For Testing Purposes Only
        elif token_tweet[i] in neg.keys():
            opinion_neg = neg[token_tweet[i]]                                   # This way you can get the opinion of token 'i' if negative
            count_negative = count_negative + 1
            #print "negative " + str(count_negative)                            # For Testing Purposes Only    
    if count_negative > count_positive:                                         # If the number of negative tokens is bigger than positive
        writefile.write('-\t' + line)                                           # Label the line as negative
    elif count_negative < count_positive:                                       # If the number of negative tokens is smaller than positive
        writefile.write('+\t' + line)                                           # Label the line as positive
    elif count_negative == count_positive:                                      # If the number of negative and positive tokens is equal
        writefile.write('0\t' + line)                                           # Label the line as neutral
    elif count_negative == 0 and count_positive == 0:                           # If the number of negative and positive tokens is zero in total
        writefile.write('undef\t' + line)                                       # Label the line as neutral
readfile.close()                                                                # Closes opened file readfile
read_neutral.close()                                                            # Closes opened file read_neutral
read_positive.close()                                                           # Closes opened file read_positive
read_negative.close()                                                           # Closes opened file read_negative
writefile.close()                                                               # Closes opened file writefile