#!/usr/bin/env python 
def missingRanges(ls):
    start = 0; end = 99
    prev = start - 1
    res = []
    for i in xrange(len(ls)+1):
        if i==len(ls):
           curr =  end+1
        else:
           curr = ls[i]
        if curr-prev >= 2:
            res.append(toRange(prev+1,curr-1))
        prev = curr 
    return res          
 
def toRange(a, b):
    if a==b:
        return str(a)
    else:
        return str(a)+"->"+str(b)

ls = [0, 1, 3, 50, 75]
print missingRanges(ls)
