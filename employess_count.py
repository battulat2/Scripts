# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 14:28:28 2019

@author: TBattula
"""
fm=0
m=0
other=0
fobj=open("C:\\Users\\tbattula\\Desktop\\Python_class\\datasets\\employees.csv", "r")

for line in fobj:

    #line1=line.split(",")

    if "Female" in line:
        fm=fm+1
    elif "Male" in line:
        m=m+1
    else:
        other=other+1
print("Female Count", fm)
print("Male Count", m)
print("Other Count", other)
    
fobj.close()