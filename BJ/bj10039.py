# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 22:19:11 2020

@author: sphil
"""


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

burger_lst = [a,b,c,d,e]
sum_score = 0

for sc in score_lst:
    if sc >= 40 :
        sum_score += sc
    else:
        sum_score += 40

print(int(sum_score/(len(score_lst))))