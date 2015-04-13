# -*- coding: utf-8 -*-
"""
@author: Niklas Bendixen
"""

import re                                                                       #import of regex
import csv                                                                      #import of csv

#read_neutral = open("germanneutral.tsv", "r")
#    for line in csv.reader(germanneutral.tsv, dialect="excel-tab")

#read_positive = open("germanpositive.tsv", "r")
#    for line in csv.reader(germanpositive.tsv, dialect="excel-tab")

#read_negative = open("germannegative.tsv", "r")
#    for line in csv.reader(germannegative.tsv, dialect="excel-tab")

readfile = open("tweetfile.txt", "r")                                           #substitute tweetfile.txt with filename
writefile = open("output.txt", "w")                                             #substitute output.txt with filename

#count_neutral = 0
#count_positive = 0
#count_negative = 0


#m = re.match(r"^A-Za-z", line)
    
for line in readfile:
    writefile.write(str(line.replace('\n', '')) + "\t\t\tneutral: " + "\tpositiv: " + "\tnegativ: \n")
    

readfile.close()                                                                #closes opened file
writefile.close()                                                               #closes opened file
#read_neutral.close()                                                           #closes opened file
#read_positive.close()                                                          #closes opened file
#read_negative.close()  
