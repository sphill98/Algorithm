# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 22:29:50 2020

@author: sphil
"""


target_str = input()
cap_target_str = target_str.upper()
str_lst = []
count_lst = []
flag = 0
max_num = 0
max_str = 'a'

for alphb in cap_target_str:
    if alphb not in str_lst:
        str_lst.append(alphb)

for a in str_lst:
    c = cap_target_str.count(a)
    count_lst.append(c)
    
for i in range(len(count_lst)):
    if max_num < count_lst[i]:
        max_num = count_lst[i]
        max_str = str_lst[i]
        flag =1
    elif max_num == count_lst[i]:
        flag = 0
    
if flag == 1:
    print (max_str)
else:
    print ('?')