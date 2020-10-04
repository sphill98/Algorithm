# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 20:42:58 2020

@author: sphil
"""

#bj2941

target_str = input()

check_lst = ['c','d','l','n','s','z']

count = 0
i = 0

while i < len(target_str):
    if target_str[i] not in check_lst:
        count += 1
    else:
        if target_str[i] == 'c':
            if i == len(target_str)-1:
                count += 1
            else:
                if (target_str[i + 1] == '=') or (target_str[i + 1] == '-'):
                    count += 1
                    i = i + 1
                else:
                    count += 1
        elif (target_str[i] == 'l') or (target_str[i] == 'n'):
            if i == len(target_str)-1:
                count += 1
            else:
                if (target_str[i + 1] == 'j'):
                    count += 1
                    i = i + 1
                else:
                    count += 1
        elif (target_str[i] == 's') or (target_str[i] == 'z'):
            if i == len(target_str)-1:
                count += 1
            else:
                if (target_str[i + 1] == '='):
                    count += 1
                    i = i + 1
                else:
                    count += 1
        elif target_str[i] == 'd':
            if i == len(target_str)-1:
                count += 1
            elif i == len(target_str) - 2:
                if (target_str[i + 1] == '-'):
                    count += 1
                    i = i + 1
                else:
                    count += 1
            elif i <= len(target_str) - 2:
                if (target_str[i + 1] == 'z') and (target_str[i + 2] == '='):
                    count += 1
                    i = i + 2
                elif (target_str[i + 1] == '-'):
                    count += 1
                    i = i + 1
                else:
                    count += 1
    i = i + 1

print(count)