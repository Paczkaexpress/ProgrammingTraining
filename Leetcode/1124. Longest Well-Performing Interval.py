# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 04:34:29 2019

@author: Erazer
"""

hours = [6,9,6]
ar = list()
ar2 = list()
flag = 0
num = 0
for i in range(len(hours)):
    if flag == 0:
        if hours[i] > 8:
            ar.append(1)
            flag = 1
        else:
            ar.append(-1)
            flag = -1
    elif flag == 1:
        if hours[i] > 8:
            ar[num] += 1
        else:
            ar.append(-1)
            num += 1
            flag = -1
    elif flag == -1:
        if hours[i] > 8:
            ar.append(1)
            num += 1
            flag = 1
        else:
            ar[num] -= 1


for i in range(len(ar)-1):
    if ar[i] > 0:
        if ar[i] > abs(ar[i+1]):
            ar2.append(ar[i] + abs(ar[i+1]))
        else:
            ar2.append(ar[i] + ar[i] -1)

    elif ar[i] < 0:
        if abs(ar[i]) > ar[i+1]:
            ar2.append(ar[i+1] + ar[i+1] -1)
        elif abs(ar[i]) == ar[i+1]:
            ar2.append(ar[i+1] + ar[i+1] -1)
        else:
            ar2.append(abs(ar[i]) + ar[i+1])

print(ar)
print(ar2)