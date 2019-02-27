# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 15:22:01 2019

@author: TBattula
"""

with open("C:\\Users\\tbattula\\Desktop\\Python_class\\datasets\\employees.csv", "r") as fobj:
    data=fobj.readlines()
    
for line in data[4:10]:
    print(line)
    