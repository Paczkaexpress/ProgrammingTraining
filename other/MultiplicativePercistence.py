# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 12:02:04 2019

@author: Mateusz Paczynski

Multiplicative percistent
"""

#get number
#convert to number, multiply
#print results

def per(number):
    counter = 0

    while len(str(number)) > 1:
        numStr = str(number)

        for i in range(len(numStr)):
            if i == 0:
                newNumber = int(numStr[0])
            else:
                newNumber = newNumber * int(numStr[i])
        counter = counter + 1
#        print(newNumber)
        number = newNumber
    print("total number of multiplicative percistent is: " + str(counter))
    return counter

numArray = [999999999999]*15

for i in range(1,1000):
    if(numArray[per(i)] > i):
        numArray[per(i)] = i

for i in range(len(numArray)):
    print("The smallest number for mult per of range: " + str(i+1) + " is: " + str(numArray[i]))
