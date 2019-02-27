# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:50:54 2019

@author: TBattula
"""

def display(*data):
    print(data)
    for items in data:
        print(items)
        
display(10,200,"Python", 'java')