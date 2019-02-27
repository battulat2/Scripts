# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:55:17 2019

@author: TBattula
"""
'''
write a program to validate the IP address.

Enter any IP  : 129.4.9
Status        : invalid IP

Enter any IP  : 124.5.43.4
Status        : valid IP

'''
'''
ip = input("Enter the IP address:")
ip_split=ip.split(".")
ip_dotcnt=list(ip.split("."))
print(ip_split)
print(ip_dotcnt)
cn
for cnt in range(0,len(ip_dotcnt)):
    
    '''
    
    ip=input('ip')
iplist=ip.split(".")
print(iplist)
cnt=0
for val in iplist:
    if int(val)<=255:
        cnt=cnt+1
if cnt>=4:
    print('valid ip')
else:
    print('invalid ip') 
    
    
    
    
    
    
    