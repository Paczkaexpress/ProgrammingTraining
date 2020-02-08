# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 04:01:26 2019

@author: Erazer
"""

arr1 = list()
arr2 = list()

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

print(arr1)

ar = list()
num = 0
for it in arr2:
    num = arr1.count(arr1[arr1.index(it)])

    print(arr1.count(arr1[arr1.index(it)]))
    for _ in range(num):
        ar.append(arr1[arr1.index(it)])
        print(arr1[arr1.index(it)])
        print(arr1.index(it))
        arr1.remove(arr1[arr1.index(it)])

arr1.sort()
ar.extend(arr1)
print(ar)
