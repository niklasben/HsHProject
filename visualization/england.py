# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:55:00 2015

@author: Niklas Bendixen
"""
import matplotlib.pyplot as plt

f = open("../SentimentAnalysis/sentiment_analysed_tweets.txt", "r")
topic = {}
pos_topic = {}
neg_topic = {}

for line in f:
    line = line.strip().replace('-','5').replace('+','10').split('\t') 

    if line[1] not in neg_topic.keys() and line[2] == 'england' and line[0] == '5':    
        neg_topic[line[1].lstrip()] = 1
    elif line[1] in neg_topic.keys() and line[2] == 'england' and line[0] == '5':
        neg_topic[line[1].lstrip()] += 1 
        
         
    if line[1] not in pos_topic.keys() and line[2] == 'england' and line[0] == '10':    
        pos_topic[line[1].lstrip()] = 1
    elif line[1] in pos_topic.keys() and line[2] == 'england' and line[0] == '10':
        pos_topic[line[1].lstrip()] += 1
    
    
#    counter = 0
#    if line[1] not in topic.keys() and line[1] != 'undef':    
#        topic[line[1].lstrip()] = 1
#    elif line[1] != 'undef' and line[1] in topic.keys():
#        topic[line[1].lstrip()] += 1  
#    counter += 1
#
#print topic
#print pos_topic
#print neg_topic

vec_pos_topic = []
index = 0
for i in pos_topic.keys():
    v = [index]*pos_topic[i]
    vec_pos_topic.extend(v)
    index += 1
 
vec_neg_topic = []
index = 0
for i in neg_topic.keys():
    v = [index]*neg_topic[i]
    vec_neg_topic.extend(v)
    index += 1

plt.figure()
x_names = [i.capitalize() for i in neg_topic.keys()]
plt.xticks(xrange(0,len(neg_topic.keys())),x_names,rotation = 90)
#plt.hist(vec_pos_topic,bins = len(pos_topic.keys()))
#plt.hist(vec_neg_topic,bins = len(neg_topic.keys()))
plt.hist([vec_pos_topic, vec_neg_topic], stacked=False, normed=False)
plt.legend(['Postive','Negative'])
plt.xlabel('Topics')
plt.ylabel('# of Tweets')
plt.show()
#plt.savefig("england_topics.png")


#bins=range(min(data), max(data) + binwidth, binwidth)