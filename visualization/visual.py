# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:53:01 2015

@author: Niklas
"""

import matplotlib.pyplot as plt
from scipy.stats import uniform

readfile = open("../SentimentAnalysis/sentiment_analysed_tweets.txt", "r")
ranking_file = open("data_ranking.txt", "w")

### Arrays
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
    if int(line[0]) == 5 or int(line[0]) == 10:
        vector = dict_all[line[2]]
        vector[topics.index(line[1])] += 1
        dict_all[line[2]] = vector

#print dict_pos
#print dict_neg
#print dict_all

### Table
#ranking_file.write('{0}\t{1}\n'.format('Countries','\t'.join(\
#[str(j) for j in topics])))
#for i in dict_all.keys():
#    ranking_file.write('{0}\t{1}\n'.format(i,'\t'.join(\
#    [str(j) for j in dict_all[i]])))

#### Plotting        
x = range(1,len(topics)+1)

color = ['red','blue','orange','black','gray','green','lightblue','brown',
'pink', 'beige', 'red','blue','orange','black','gray','green','lightblue','brown',
'pink', 'beige', 'red','blue','orange','black','gray','green','lightblue','brown',
'pink', 'beige']

index = 0
fig = plt.figure()
ax1 = fig.add_subplot(211)

for i in dict_pos.keys():
    ax1.plot(x, uniform.cdf(list(dict_pos[i]), loc = 0, scale = \
    max(list(dict_pos[i]))), color[index], linestyle = '-', marker = 'o',\
             markersize = 6.0)
    index += 1
plt.legend(title = 'Positive Opinion')
ax2 = fig.add_subplot(212)
index = 0

for i in dict_neg.keys():
    ax2.plot(x, uniform.cdf(list(dict_neg[i]), loc = 0, scale = \
    max(list(dict_neg[i]))), color[index], linestyle = '-', marker = 'o',\
             markersize = 6.0)
    index += 1
my_xticks = topics
plt.xticks(x, my_xticks, rotation=90)
plt.legend(['Negative Opinion'])
ax1.legend(dict_pos.keys(), loc = 'center left', bbox_to_anchor = (1.1, -0.7), fancybox = True, shadow = True)
plt.show()


readfile.close()
ranking_file.close()