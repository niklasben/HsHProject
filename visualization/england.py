# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:55:00 2015

@author: Niklas Bendixen
"""
import numpy as np
import matplotlib.pyplot as plt
import pylab
from scipy.stats import uniform

f = open("../SentimentAnalysis/sentiment_analysed_tweets.txt", "r")

#topic = {}
pos_topic = {}
neg_topic = {}

for line in f:
    line = line.strip().replace('-','5').replace('+','10').split('\t') 

    if line[1] not in neg_topic.keys() and line[2] == 'england' and line[0] == '5':
        neg_topic[line[1].lstrip()] = 1
    elif line[1] in neg_topic.keys() and line[2] == 'england' and line[0] == '5':
        neg_topic[line[1].lstrip()] += 1
    elif line[1] not in neg_topic.keys() and line[2] == 'england':
        neg_topic[line[1].lstrip()] = 0
        
         
    if line[1] not in pos_topic.keys() and line[2] == 'england' and line[0] == '10':    
        pos_topic[line[1].lstrip()] = 1
    elif line[1] in pos_topic.keys() and line[2] == 'england' and line[0] == '10':
        pos_topic[line[1].lstrip()] += 1
    elif line[1] not in pos_topic.keys() and line[2] == 'england':
        pos_topic[line[1].lstrip()] = 0
    
    
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
#print neg_topic.values()

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

x_names = []
for i in xrange(0, len(neg_topic.keys())):
#    if (i %2 != 0):
    x_names.append(neg_topic.keys()[i])
#    x_names.append(" ")
#    else:
#        x_names.append(" ")

#plt.figure()
#x_names = [i.capitalize() for i in neg_topic.keys()]
#plt.xticks(xrange(0,len(neg_topic.keys())),x_names,rotation = 90)
#plt.hist(vec_pos_topic,bins = len(pos_topic.keys()))
#plt.hist(vec_neg_topic,bins = len(neg_topic.keys()))
#plt.hist([vec_pos_topic, vec_neg_topic], stacked=False, normed=False)
#plt.legend(['Postive','Negative'])
#plt.xlabel('Topics')
#plt.ylabel('# of Tweets')


#print x_names


##########################
N = 25

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, pos_topic.values(), width, color='g')

rects2 = ax.bar(ind+width, neg_topic.values(), width, color='r')

# add some text for labels, title and axes ticks
ax.set_ylabel('# of Tweets')
#plt.xlabel('Topics')
ax.set_title('England')
ax.set_xticks(ind+width)
ax.set_xticklabels(x_names,rotation = 60)
#ax.set_xticklabels(x_names)

ax.legend( (rects1[0], rects2[0]), ('Positive', 'Negative') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
############################








plt.show()
#plt.savefig("england_topics.png")


#bins=range(min(data), max(data) + binwidth, binwidth)