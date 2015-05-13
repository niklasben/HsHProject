import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform 

f = open('C:\StudentsProject\sentiment_analysed_tweets.txt')

topic = {}
pos_countries = {}
neg_countries = {}

for line in f:
    line = line.strip().replace('-','5').replace('+','10').split('\t') 
    
    if line[2] not in neg_countries.keys() and line[1] == 'Regierung/Politik/Recht' and line[0] == '5':    
        neg_countries[line[2].lstrip()] = 1
    elif line[2] in neg_countries.keys() and line[1] == 'Regierung/Politik/Recht' and line[0] == '5':
        neg_countries[line[2].lstrip()] += 1 
        
         
    if line[2] not in pos_countries.keys() and line[1] == 'Regierung/Politik/Recht' and line[0] == '10':    
        pos_countries[line[2].lstrip()] = 1
    elif line[2] in pos_countries.keys() and line[1] == 'Regierung/Politik/Recht' and line[0] == '10':
        pos_countries[line[2].lstrip()] += 1        
    
    
vec_pos_topic = []
index = 0
for i in pos_countries.keys():
    v = [index]*pos_countries[i]
    vec_pos_topic.extend(v)
    index += 1
 
    
vec_neg_topic = []
index = 0
for i in neg_countries.keys():
    v = [index]*neg_countries[i]
    vec_neg_topic.extend(v)
    index += 1
    
                        
#x_names = [i.capitalize() for i in topic.keys()]
#plt.xticks(xrange(0,len(topic.keys())),x_names,rotation = 45)  
plt.hist(vec_pos_topic,bins = len(pos_countries.keys())) 
plt.hist(vec_neg_topic,bins = len(neg_countries.keys())) 
plt.legend('Regierung/Politik/Recht') 
plt.legend(['Postive','Negative']) 
plt.xlabel('Countries')            
plt.ylabel('# of Tweets') 
plt.show()
plt.savefig('C:\StudentsProject\Topic_Regierung.png')
