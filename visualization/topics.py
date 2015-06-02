# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:12:27 2015

@author: Niklas Bendixen
"""
import matplotlib.pyplot as plt

f = open("../SentimentAnalysis/sentiment_analysed_tweets.txt", "r")

topic = {}
countries = {}
counter = 0
for line in f:
    line = line.strip().split('\t')     #.replace('-','5').replace('+','10')
    
    if line[1] not in topic.keys() and line[1] != 'undef':    
        topic[line[1].lstrip()] = 1
    elif line[1] != 'undef' and line[1] in topic.keys():
        topic[line[1].lstrip()] += 1  
    counter += 1    
#x = range(1,len(topic)+1)
vec = []
index = 0
for i in topic.keys():
    v = [index]*topic[i]
    vec.extend(v)
    index += 1
x_names = [i.capitalize() for i in topic.keys()]
plt.xticks(xrange(0,len(topic.keys())),x_names,rotation = 90)  
plt.hist(vec,bins = len(topic.keys()))  
plt.xlabel('Topics')            
plt.ylabel('# of Tweets') 
plt.show()
#plt.savefig('topics.png')