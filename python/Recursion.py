#!/usr/bin/env python

def r_sum(nest_list):
    tot = 0
    for ele in nest_list:
        if type(ele) == type([]):
            tot += r_sum(ele)
        else:
            tot += ele
    return tot

def r_max(nest_list):
    largest = None
    for e in nest_list:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e
        if val > largest:
            largest = val
           
    return largest

#arr = [[[13, 7], 90], 2, [1, 100], 8, 6]
arr = [2, [[100, 7], 90], [1, 13], 8, 6]
print r_sum(arr)
print r_max(arr)
