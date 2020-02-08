# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 23:05:22 2019

@author: Erazer
@task: Interview question. To find number close to given one:
    https://www.youtube.com/watch?v=GBuHSRDGZBY
"""

arr1 = [-1, 3, 8, 2, 9, 5]
arr2 = [4,1,2,10,5,20]

target = 24

arr3 = arr1

for i in range(len(arr3)):
    arr3[i] = target - arr3[i]

print(arr3)