#!/usr/bin/env python

def binarysearch(arr, target):
    begin = 0
    end = len(arr)-1
    while begin<end:
        mid = (begin+end)/2
        if target==arr[mid]:
            return True
        if target>arr[mid]:
            begin = mid+1
        else:
            end = mid-1
    return False

arr = [1, 3, 5, 9, 13]
print binarysearch(arr, 43)
