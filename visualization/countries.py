# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:09:31 2015

@author: Niklas
"""
import matplotlib.pyplot as plt

f = open("../SentimentAnalysis/sentiment_analysed_tweets.txt", "r")

countries = {}
counter = 0
for line in f:
    line = line.strip().split('\t')
    
    if line[2] not in countries.keys():
        countries[line[2]] = 1 
    else:
        countries[line[2]] += 1
    counter += 1
           
countries_array = []    
index = 0
for i in countries.keys():
    v = [index]*countries[i]
    countries_array.extend(v)
    index += 1    

x_names = [i.capitalize() for i in countries.keys()]
plt.xticks(range(0,len(countries.keys())),x_names,rotation = 90)  
plt.hist(countries_array,bins = len(countries.keys()))
plt.xlabel('Countries')            
plt.ylabel('Frequency') 
plt.show()
#plt.savefig('countries.png')