# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:41:03 2019

@author: TBattula
"""


# Function body
def add(first=0, second=0, third=0):
    total=first + second + third
    return total


print("Code Starts")
gettotal =add(10,20)
print(gettotal)

gettotal =add(10,30, 30)
print(gettotal)
gettotal =add(200)
print(gettotal)
print("Code ends")