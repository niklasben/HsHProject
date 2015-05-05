# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:53:01 2015

@author: Niklas
"""

import matplotlib.pyplot as plt
import numpy as np


readfile = open("../SentimentAnalysis/sentiment_analysed_tweets.txt", "r")
#writefile = open("data_visual.txt", "w")

### Arrays
color = ['red','blue','orange','black','gray','green','lightblue','brown',
'pink', 'beige', 'buff', 'chartreuse', 'citrine', 'cream', 'darkgoldenrod',
'applegreen', 'artichoke','amber', 'apricot','arylideyellow', 'aureolin', 
'asparagus', 'avocado', 'brightgreen', 'cal', 'polygreen']

countries = []
topics = []

for line in readfile:
    line = line.strip().replace("\xfc", "ue").replace("\xe4", "ae").split('\t')
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

readfile = open("../SentimentAnalysis/sentiment_analysed_tweets.txt", "r")

for line in readfile:
    line = line.strip().replace('-','5').replace('+','10')\
        .replace("\xfc", "ue").replace("\xe4", "ae").split('\t')
    if int(line[0]) == 10 and int(line[0]) != 0:
        vector = dict_pos[line[2]]
        vector[topics.index(line[1])] += 1
        dict_pos[line[2]] = vector
    elif int(line[0]) == 5 and int(line[0]) != 0:
        vector = dict_neg[line[2]]
        vector[topics.index(line[1])] += 1
        dict_neg[line[2]] = vector
    elif int(line[0]) == 5 or int(line[0]) != 0:
        vector = dict_all[line[2]]
        vector[topics.index(line[1])] += 1
        dict_all[line[2]] = vector

### Plotting        
x = range(1,len(topics)+1)
#y = range(1,len(countries)+1)
#print y



index = 0
fig = plt.figure()
ax1 = fig.add_subplot(211)

for i in dict_pos.keys():
    ax1.plot(x, list(dict_pos[i]),color[2],linestyle = '-', marker = 'o',\
             markersize = 7.0)
    index += 1
    plt.legend(['Positive Opinion'])
    ax2 = fig.add_subplot(212)
    index = 0

for i in dict_neg.keys():
    ax2.plot(x, list(dict_neg[i]),color[7],linestyle = '-', marker = 'o',\
             markersize = 7.0)
    index += 1
    my_xticks = topics
    plt.xticks(x, my_xticks, rotation=90)
    plt.legend(['Negative Opinion'])
    plt.show()













#####################################################################


#readfile = open("../SentimentAnalysis/sentiment_analysed_tweets.txt", "r")
#
#for line in readfile:
#    line = line.strip().split('\t')
#    countries[line[2]].set
#    topics.index(line[2])











#for i in countries:
#    for u in topics:
#        both.append((i, u))
#        print both



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