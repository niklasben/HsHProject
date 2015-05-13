# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:41:12 2015

@author: Niklas
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform 

f = open("../SentimentAnalysis/sentiment_analysed_tweets.txt", "r")

topic = {}
pos_topic = {}
neg_topic = {}

for line in f:
    line = line.strip().replace('-','5').replace('+','10').split('\t') 
    
    if line[1] not in neg_topic.keys() and line[2] == 'england' and line[0] == '-':    
        neg_topic[line[1].lstrip()] = 1
    elif line[1] in neg_topic.keys() and line[2] == 'england' and line[0] == '-':
        neg_topic[line[1].lstrip()] += 1 
        
         
    if line[1] not in pos_topic.keys() and line[2] == 'england' and line[0] == '+':    
        pos_topic[line[1].lstrip()] = 1
    elif line[1] in pos_topic.keys() and line[2] == 'england' and line[0] == '+':
        pos_topic[line[1].lstrip()] += 1        
    
print neg_topic    
#x = range(1,len(topic)+1)
'''
vec = []
index = 0
for i in neg_countries.keys():
    v = [index]*topic[i]
    vec.extend(v)
    index += 1
    
x_names = [i.capitalize() for i in topic.keys()]
#plt.xticks(xrange(0,len(topic.keys())),x_names,rotation = 45)  
plt.hist(vec,bins = len(topic.keys()))  
plt.xlabel('Topics')            
plt.ylabel('Frequency') 
plt.show()
plt.savefig('C:\StudentsProject\Topics.png')
'''