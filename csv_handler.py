# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 16:30:53 2019

@author: TBattula
"""
'''
import csv
fobj=open("employees.csv","r")
reader = csv.reader(fobj)
for line in reader:
    '''
    
import csv
with open("C:\\Users\\tbattula\\Desktop\\Python_class\\datasets\\employees.csv", "r") as fobj:
    reader = csv.reader(fobj)
    for line in reader:
        print(line)