# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 22:29:17 2020

@author: sphil
"""


b1 = int(input())
b2 = int(input())
b3 = int(input())
d1 = int(input())
d2 = int(input())

burger_lst = [b1,b2,b3]
drink_lst = [d1,d2]
set_lst = []

for bg in burger_lst:
    for dr in drink_lst:
        set_lst.append(bg+dr-50)

print(int(min(set_lst)))