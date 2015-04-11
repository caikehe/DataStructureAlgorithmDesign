#!/usr/bin/env python 
def listsum(numlist):
    sum = 0
    for item in numlist:
        sum += item
    return sum

def listsum1(numlist):
    if len(numlist) == 1:
        return numlist[0]
    return numlist[0] + listsum1(numlist[1:])

print(listsum1([1,3,5,7,9]))

