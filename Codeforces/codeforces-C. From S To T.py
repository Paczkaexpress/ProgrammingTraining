# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 16:46:18 2019

@author: Erazer
"""

test = int(input())

for _ in range(test):
    s = input()
    t = input()
    p = input()

    for i in p:
        t = t.replace(i,'',1)

    for i in s:
        t = t.replace(i,'',1)

    if(len(t) == 0):
        print('YES')
    else:
        print('NO')