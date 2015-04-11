#!/usr/bin/env python 

def twoSum(sList, target):
    #use double pointers
    l = len(sList)
    first = 0; end = l-1
    while first < l and end >= 0:
        s = sList[first] + sList[end]
        if s > target:
            end -= 1
        elif s < target:
            first += 1
        else:
            return (first+1, end+1)

sList = [2, 7, 11, 15]
target = 18
print twoSum(sList, target)
     
