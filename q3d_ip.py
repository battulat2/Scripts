# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 17:12:25 2019

@author: TBattula
"""
'''
192.168.0.10
192.168.1.0
192.168.1.1
192.168.1.2
192.168.1.3
..
..
192.168.1.10



fixed ="192.168."

for val in range(0,2):
    subip ="192.168."+str(val)
    for val in range(1,100):
        print(subip+"."+str(val))
        
'''

list1=[]
list2=[]
fixed ="192.168."
for val in range(1,100):
    list1.append(fixed+"0."+str(val))
    list2.append(fixed+"1."+str(val))
for ip in list1:
    print(ip)
for ip in list2:
    print(ip)
    