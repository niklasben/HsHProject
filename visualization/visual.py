# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:53:01 2015

@author: Niklas Bendixen
"""
import pylab as P
import matplotlib.pyplot as plt
#from matplotlib import figure
import pylab
from scipy.stats import uniform
from sklearn import preprocessing
import sys

readfile = open("../SentimentAnalysis/sentiment_analysed_tweets.txt", "r")
ranking_file_all = open("data_ranking_all.txt", "w")
ranking_file_pos = open("data_ranking_pos.txt", "w")
ranking_file_neg = open("data_ranking_neg.txt", "w")

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

### Tables
ranking_file_all.write('{0}\t{1}\n'.format('Countries','\t'.join(\
[str(j) for j in topics])))
for i in dict_all.keys():
    ranking_file_all.write('{0}\t{1}\n'.format(i,'\t'.join(\
    [str(j) for j in dict_all[i]])))
    
ranking_file_pos.write('{0}\t{1}\n'.format('Countries','\t'.join(\
[str(j) for j in topics])))
for i in dict_pos.keys():
    ranking_file_pos.write('{0}\t{1}\n'.format(i,'\t'.join(\
    [str(j) for j in dict_pos[i]])))


ranking_file_neg.write('{0}\t{1}\n'.format('Countries','\t'.join(\
[str(j) for j in topics])))
for i in dict_neg.keys():
    ranking_file_neg.write('{0}\t{1}\n'.format(i,'\t'.join(\
    [str(j) for j in dict_neg[i]])))

### Plotting        
x = range(1,len(topics)+1)

color = ['#FF0000','#0000FF','#FFA500','#000000','#BEBEBE','#00FF00','#8470FF',
'#A52A2A', '#FFC0CB', '#F5F5DC', '#EEDFCC', '#E6E6FA', '#00BFFF', '#00FF7F',
'#FFD700', '#CD5C5C', '#FF6347', '#D8BFD8', '#556B2F', '#FFE4E1', '#E0EEE0',
'#2F4F4F', '#CAFF70', '#DA70D6']

index = 0
fig = plt.figure()
ax1 = fig.add_subplot(211)

for i in dict_pos.keys():
    ax1.plot(x, uniform.cdf(list(dict_pos[i]), loc = 0, scale = \
    max(list(dict_pos[i]))), color[index], linestyle = '-', marker = 'o',\
             markersize = 6.0)
    index += 1
#plt.legend(['Positive Opinion'])
ax2 = fig.add_subplot(212)
index = 0

for i in dict_neg.keys():
    ax2.plot(x, uniform.cdf(list(dict_neg[i]), loc = 0, scale = \
    max(list(dict_neg[i]))), color[index], linestyle = '-', marker = 'o',\
             markersize = 6.0)
    index += 1
my_xticks = topics
plt.xticks(x, my_xticks, rotation = 90)
#ax2.legend(['Negative Opinion'])
ax1.legend(dict_pos.keys(), loc = 'center left', bbox_to_anchor = (1.1, -0.7),\
fancybox = True, shadow = True)
plt.show()

### Histogram
file_hist = open("data_ranking.txt", "r")


hist = []

for line in file_hist:
    if line[0] not in countries:
        countries.append(line[2])
    if line[1] not in topics:
        topics.append(line[1])


dict_hist = {}

for i in countries:
    dict_hist[i] = [0]*len(topics)



for line in file_hist:
    line = line.strip().replace('-','5').replace('+','10')\
        .replace("\xfc", "ue").replace("\xe4", "ae").split('\t')

#first create a single histogram

mu, sigma = 200, 25
x = mu + sigma*P.randn(10000)

#the histogram of the data with histtype='step'
n, bins, patches = P.hist(x, 50, normed=1, histtype='stepfilled')
P.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

#add a line showing the expected distribution
y = P.normpdf( bins, mu, sigma)
l = P.plot(bins, y, 'k--', linewidth=1.5)

P.figure()

#create a new data-set
x = mu + sigma*P.randn(1000,3)

n, bins, patches = P.hist(x, 10, normed=1, histtype='bar',
                            color=['crimson', 'burlywood', 'chartreuse'],
                            label=['Crimson', 'Burlywood', 'Chartreuse'])
P.legend()









readfile.close()
ranking_file_all.close()
ranking_file_pos.close()
ranking_file_neg.close()
file_hist.close()