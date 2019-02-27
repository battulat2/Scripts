# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 09:07:23 2019

@author: TBattula

alist = ["google","unix","facebook","linkedin"]
write a program to read the above list and add "http://www" at the beginning
and append ".com" at the end of each element.

http://www.google.com
http://www.unix.com
http://www.facebook.com
http://www.linkedin.com
"""

f1="http://www."
f2=".com"

alist = ["google","unix","facebook","linkedin"]

print(len(alist))

val=0

for val in range(0,len(alist)):
    fianl=f1+alist[val]+f2
    print(fianl)
    val=val+1
print("end")
    
    

