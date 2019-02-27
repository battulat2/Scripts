# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:50:47 2019

@author: TBattula
"""

print(list(range(1,10)))

print(tuple(range(3,9)))
print(list(range(2,10,2)))

name1=input("enter name")
x=len(name1)

if len(name1)<10:
    print("Too small")
elif len(name1)>30:
    print("Too big")