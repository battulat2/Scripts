# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 16:13:16 2019

@author: TBattula
"""
'''
print(os.getlogin)

import os
import glob


extension = 'csv'
os.chdir(path)
result = [i for i in glob.glob('*.{}'.format(extension))]
print(result)
'''
x=os.listdir("C:\\Users\\tbattula\\Desktop\\Python_class\\datasets")
x1=list(x)
y=len(x)
print(y)
for val in (0,len(x)):
    if str(x) in (".csv"):
        print(x)
    
