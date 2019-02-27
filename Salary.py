# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 14:36:06 2019

@author: TBattula
"""

fobj=open("C:\\Users\\tbattula\\Desktop\\Python_class\\datasets\\employees.csv", "r")
header=fobj.readline() #ignore header
count=0
#filename=time.strftime("%d_%b_%Y)
for line in fobj:
    line=line.strip()
    line1 = line.split(",")
    l2=list(line1)
    if int(l2[4]) > 100000  :
        print(line)
    if count==5:
        break
    count=count+1
    
fobj.close()