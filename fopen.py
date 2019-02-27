# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 12:48:49 2019

@author: TBattula
"""

fobj = open("demo.txt","r")

for line in fobj:
    line=line.strip() #remove extra space
   # print(line)
    data=line.split()
    print(data[0])
fobj.close()