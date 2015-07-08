# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:55:00 2015

@author: Niklas Bendixen
"""
import numpy as np 
import matplotlib.pyplot as plt
#import pylab
#from scipy.stats import uniform
#from sklearn.preprocessing import normalize
#from sklearn import preprocessing
#from decimal import Decimal
#import math

f = open("../SentimentAnalysis/sentiment_analysed_tweets.txt", "r")

topic = {}
pos_topic = {}
neg_topic = {}
neu_topic = {}

for line in f:
    line = line.strip().replace('-','5').replace('+','10').split('\t') 

    if line[1] not in neg_topic.keys() and line[1] != 'undef' and line[2] \
    == 'uk' and line[0] == '5':
        neg_topic[line[1].lstrip()] = 1
    elif line[1] in neg_topic.keys() and line[1] != 'undef' and line[2] \
    == 'uk' and line[0] == '5':
        neg_topic[line[1].lstrip()] += 1
    elif line[1] not in neg_topic.keys() and line[1] != 'undef' and line[2] \
    == 'uk':
        neg_topic[line[1].lstrip()] = 0
         
    if line[1] not in pos_topic.keys() and line[1] != 'undef' and line[2] \
    == 'uk' and line[0] == '10':    
        pos_topic[line[1].lstrip()] = 1
    elif line[1] in pos_topic.keys() and line[1] != 'undef' and line[2] \
    == 'uk' and line[0] == '10':
        pos_topic[line[1].lstrip()] += 1
    elif line[1] not in pos_topic.keys() and line[1] != 'undef' and line[2] \
    == 'uk':
        pos_topic[line[1].lstrip()] = 0
    
    if line[1] not in neu_topic.keys() and line[1] != 'undef' and line[2] \
    == 'uk' and line[0] == '0':    
        neu_topic[line[1].lstrip()] = 1
    elif line[1] in neu_topic.keys() and line[1] != 'undef' and line[2] \
    == 'uk' and line[0] == '0':
        neu_topic[line[1].lstrip()] += 1
    elif line[1] not in neu_topic.keys() and line[1] != 'undef' and line[2] \
    == 'uk':
        neu_topic[line[1].lstrip()] = 0



#print topic
#print pos_topic
#print neg_topic
#print neg_topic.keys()
#print pos_topic.values()
#print neg_topic.values()
#print neu_topic.values()


#for i in pos_topic.keys():
#    float(pos_topic[i])
#    print pos_topic[i]


#norm = [float(i)/sum(pos_topic.values()) for i in pos_topic]
#print norm



#a = np.array(neg_topic.values())
#mag_a = np.sqrt(sum([i*i for i in a]))
#a = np.array(a)/mag_a
##print a #np.linalg.norm(a)
#b = np.array(pos_topic.values())
#mag_b = np.sqrt(sum([i*i for i in b]))
#b = np.array(b)/mag_b
#
#c = np.array(neu_topic.values())
#c[6] = 33000
##print c
#mag_c = np.sqrt(sum([i*i for i in c]))
##print mag_c
#c = np.array(c)/mag_c
##print c





#total_topic = (np.array(pos_topic.values()))+(np.array(neg_topic.values()))+(np.array(neu_topic.values()))
#posx = (np.array(pos_topic.values()))
#print total_topic
#print posx
#test = posx / total_topic
#print test



###Normalized Data
#pos = total_countries*np.array(pos_countries.values())/100
#neg = ((np.array(total_countries.values())*np.array(neg_countries.values()))/100)
#neu = ((np.array(total_countries.values())*np.array(neu_countries.values()))/100)
#print total_countries
#print pos


#nr = total_countries.values()/pos_countries.values()*100
#print nr


pos_topic_vector = []
index = 0
for i in pos_topic.keys():
    v = [index]*pos_topic[i]
    pos_topic_vector.extend(v)
    index += 1
 
neg_topic_vector = []
index = 0
for i in neg_topic.keys():
    v = [index]*neg_topic[i]
    neg_topic_vector.extend(v)
    index += 1

neu_topic_vector = []
index = 0
for i in neu_topic.keys():
    v = [index]*neu_topic[i]
    neu_topic_vector.extend(v)
    index += 1

#print pos_topic_vector

x_names = []
for i in xrange(0, len(neg_topic.keys())):
#    if (i %2 != 0):
        x_names.append(neg_topic.keys()[i])
#        x_names.append(" ")
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
#
#
#print x_names




##########################
N = 24

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(ind, pos_topic.values(), width, color='g')
rects2 = ax.bar(ind+width, neg_topic.values(), width, color='r')
#rects3 = ax.bar(ind+width+width, neu_topic.values(), width, color='b')

#rects1 = ax.bar(ind, b, width, color='g')
#rects2 = ax.bar(ind+width, a, width, color='r')
#rects3 = ax.bar(ind+width+width, c, width, color='b')


#add some text for labels, title and axes ticks
ax.set_ylabel('# of Tweets')
#plt.xlabel('Topics')
ax.set_title('England / Topics', fontsize=20)
ax.set_xticks(ind+width*1.5)
ax.set_xticklabels(x_names,rotation = 90)
#ax.set_xticklabels(x_names)

#ax.legend( (rects1[0], rects2[0], rects3[0]), ('Positive', 'Negative', 'Neutral') )
ax.legend( (rects1[0], rects2[0]), ('Positive', 'Negative') )

#def autolabel(rects):
#    # attach some text labels
#    for rect in rects:
#        height = rect.get_height()
#        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
#                ha='center', va='bottom')


                

#autolabel(rects1)
#autolabel(rects2)
#autolabel(rects3)
############################








plt.show()
#plt.savefig("england_topics.png")


#bins=range(min(data), max(data) + binwidth, binwidth)