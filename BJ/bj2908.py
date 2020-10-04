# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 22:53:08 2020

@author: sphil
"""

target = input()
str_lst = target.split()
num_lst = []

for i in str_lst:
    num_lst.append(int(i))

a = num_lst[0]
b = num_lst[1]

if (a%100)>(b%100):
    
    if (int((a%10)/10))>=(int((a%10)/10)):
        if a>=b:
            
