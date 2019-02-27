# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:53:20 2019

@author: TBattula
"""
'''
alist = ["google","unix","facebook","linkedin"]

write a program to read the above list and add "http://www" at the beginning
and append ".com" at the end of each element.

http://www.google.com
http://www.unix.com
http://www.facebook.com
http://www.linkedin.com
'''

alist = ["google","unix","facebook","linkedin"]

fixed1="http://www."
fixed2=".com"

print(alist.split('.'))