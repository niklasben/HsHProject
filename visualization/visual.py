# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:53:01 2015

@author: Niklas
"""

#import pandas as pd
#from sklearn import ensemble
#import matplotlib.pyplot as plt
#import numpy

readfile = open("../SentimentAnalysis/sentiment_analysed_tweets.txt", "r")
#writefile = open("data_visual.txt", "w")

### Arrays
countries = []
topics = []

for line in readfile:
    line = line.strip().replace("\xfc", "ue").replace("\xe4", "ae").split('\t')
    if line[2] not in countries:
        countries.append(line[2])
    if line[1] not in topics:
        topics.append(line[1])
            


dict_all = {}
dict_pos = {}
dict_neg = {}
for j in countries:
    dict_all[j] = [0]*len(topics)
    dict_pos[j] = [0]*len(topics)
    dict_neg[j] = [0]*len(topics)



readfile = open("../SentimentAnalysis/sentiment_analysed_tweets.txt", "r")

for line in readfile:
    line = line.strip().split('\t')
    countries[line[2]].set
    topics.index(line[2])











#for i in countries:
#    for u in topics:
#        both.append((i, u))
#        print both


#print countries
#print topics
#print d



#countries = set(countries)
#topics = set(topics)


#vector = []
#
#readfile = open("../SentimentAnalysis/sentiment_analysed_tweets.txt", "r")
#
#
#
#for line in readfile:
#    line = line.strip().replace("+", "10").replace("-", "5").split('\t')
#    if line[1] in topics and line[2] in countries[len(countries)-1]:
#        if int(line[0]) != 0:
#            vector.append(line[0])

#print vector

readfile.close()
#writefile.close()