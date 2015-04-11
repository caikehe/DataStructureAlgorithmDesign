#!/usr/bin/env python

def removeDuplicates(ls):
    if len(ls) == 0:
        return 0
    slow = fast = 1
    while fast < len(ls):
        if ls[fast] != ls[fast-1]:
            ls[slow] = ls[fast]
            slow += 1
        fast += 1
    #return slow
    return ls[:]

ls = [1, 1, 2, 2, 2, 2, 8, 8]
print removeDuplicates(ls)
