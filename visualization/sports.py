# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 10:04:00 2015

@author: Niklas
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 19 10:54:00 2015

@author: Niklas Bendixen
"""
import numpy as np
import matplotlib.pyplot as plt
#import pylab
#from scipy.stats import uniform
#from sklearn import preprocessing

f = open('../SentimentAnalysis/sentiment_analysed_tweets.txt')

topic = {}
pos_countries = {}
neg_countries = {}
neu_countries = {}
#total_countries = {}

for line in f:
    line = line.strip().replace('-','5').replace('+','10').split('\t') 
    
    if line[2] not in neg_countries.keys() and line[1] == 'Sport' and line[0] == '5':    
        neg_countries[line[2].lstrip()] = 1
        #total_countries[line[2].lstrip()] = 1
    elif line[2] in neg_countries.keys() and line[1] == 'Sport' and line[0] == '5':
        neg_countries[line[2].lstrip()] += 1
        #total_countries[line[2].lstrip()] += 1
         
    if line[2] not in pos_countries.keys() and line[1] == 'Sport' and line[0] == '10':    
        pos_countries[line[2].lstrip()] = 1
        #total_countries[line[2].lstrip()] = 1
    elif line[2] in pos_countries.keys() and line[1] == 'Sport' and line[0] == '10':
        pos_countries[line[2].lstrip()] += 1
        #total_countries[line[2].lstrip()] += 1
        
    if line[2] not in neu_countries.keys() and line[1] == 'Sport' and line[0] == '0':    
        neu_countries[line[2].lstrip()] = 1
        #total_countries[line[2].lstrip()] = 1
    elif line[2] in neu_countries.keys() and line[1] == 'Sport' and line[0] == '0':
        neu_countries[line[2].lstrip()] += 1
        #total_countries[line[2].lstrip()] += 1

#print pos_countries
#print pos_countries.values()
#print neg_countries
#print neg_countries.values()
#print neu_countries
#print neu_countries.values()
#print total_countries
#print total_countries.values()

#total_countries = (np.array(pos_countries.values()))+(np.array(neg_countries.values()))+(np.array(neu_countries.values()))
###Normalized Data
#pos = total_countries*np.array(pos_countries.values())/100
#neg = ((np.array(total_countries.values())*np.array(neg_countries.values()))/100)
#neu = ((np.array(total_countries.values())*np.array(neu_countries.values()))/100)
#print total_countries
#print pos


#nr = total_countries.values()/pos_countries.values()*100
#print nr
    
pos_countries_vector = []
index = 0
for i in pos_countries.keys():
    v = [index]*pos_countries[i]
    pos_countries_vector.extend(v)
    index += 1
 
    
neg_countries_vector = []
index = 0
for i in neg_countries.keys():
    v = [index]*neg_countries[i]
    neg_countries_vector.extend(v)
    index += 1

neu_countries_vector = []
index = 0
for i in neu_countries.keys():
    v = [index]*neu_countries[i]
    neu_countries_vector.extend(v)
    index += 1



a = np.array(neg_countries.values())
mag_a = np.sqrt(sum([i*i for i in a]))
a = np.array(a)/mag_a
print a #np.linalg.norm(a)
b = np.array(pos_countries.values())
mag_b = np.sqrt(sum([i*i for i in b]))
b = np.array(b)/mag_b
print b
#
#c = np.array(neu_countries.values())
#c[6] = 33000
##print c
#mag_c = np.sqrt(sum([i*i for i in c]))
##print mag_c
#c = np.array(c)/mag_c
##print c



x_names = []
for i in xrange(0, len(neg_countries.keys())):
#    if (i %2 != 0):
    x_names.append(neg_countries.keys()[i])
#    x_names.append(" ")
#    else:
#        x_names.append(" ")


#print pos_countries_vector
#print len(neg_countries.keys())
#print len(pos_countries.keys())#
#print x_names

#plt.figure()                       
#x_names = [i.capitalize() for i in xrange(0,neg_countries.keys()) if (i %2 == 0)]
#plt.xticks(xrange(0,len(neg_countries.keys())),x_names,rotation = 90)  
#plt.hist(vec_pos_topic,bins = len(pos_countries.keys())) 
#plt.bar(xrange(0,len(neg_countries.keys())),neg_countries.values())
#plt.hist([pos_countries_vector, neg_countries_vector], stacked=False, normed=False)
#plt.legend('Politik') 
#plt.legend(['Postive','Negative'])
#plt.xlabel('Countries')            
#plt.ylabel('# of Tweets')

##########################
N = 21

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars


fig, ax = plt.subplots()

rects1 = ax.bar(ind, pos_countries.values(), width, color='g')
#rects1 = ax.bar(ind, a, width, color='g')

rects2 = ax.bar(ind+width, neg_countries.values(), width, color='r')
#rects2 = ax.bar(ind+width, b, width, color='r')

#rects3 = ax.bar(ind+width+width, neu_countries.values(), width, color='b')

# add some text for labels, title and axes ticks
ax.set_ylabel('# of Tweets')
#plt.xlabel('Countries')
ax.set_title('Label \"Sport\" fuer alle Laender', fontsize=20)
ax.set_xticks(ind+(width*1.5))
ax.set_xticklabels(x_names,rotation = 60)
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


plt.show()
#plt.savefig('sports.png')