# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 01:50:25 2020

@author: sphil
"""

N = input()
N_lst = N.split()
N_int_lst = []

for i in N_lst:
    N_int_lst.append(int(i))
    
A = N_int_lst[0]
B = N_int_lst[1]
C = N_int_lst[2]

if B!=C:
    if C-B<=0:
        print(-1)
    else:
        print(int(A/(C-B))+1)
else:
    print(-1)
