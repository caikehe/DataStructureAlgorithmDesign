#!/usr/bin/env python 

def remove_adjacent_dups(x):
    result = []
    most_recent_ele = None
    for item in x:
        if item != most_recent_ele:
            result.append(item)
            most_recent_ele = item
    return result

#the list shoould be sorted first
arr = [1,2,3,3,3,3,5,6,9,9]
print remove_adjacent_dups(arr)
