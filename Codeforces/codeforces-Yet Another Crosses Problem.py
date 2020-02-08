# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 16:11:55 2019

@author: Erazer
"""

test = int(input())

for _ in range(test):
    N,M = map(int, input().split())
    ar = list([input() for _ in range(N)])

    xFlag = False
    yFlag = False
    couter = 0
    countMaxX = 0
    countMaxY = 0
    for i in ar:
        couter = i.count('*')
        countMaxX = max(couter,countMaxX)

    ar = zip(*ar)
    for i in ar:
        couter = i.count('*')
        countMaxY = max(couter,countMaxY)

    print(N+M-countMaxY-countMaxX)