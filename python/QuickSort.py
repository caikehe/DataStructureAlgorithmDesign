#!/usr/bin/env python 

def partition(ls, l, r):
    # choose the last element as pivot
    pivot = ls[r]
    #due to the fact that we input the full array every time,
    #beware of the lower and upper label of this range
    for i in xrange(l, r):
        if ls[i] < pivot:
            ls[l], ls[i] = ls[i], ls[l]
            l += 1
    # put pivot in the right position
    ls[r], ls[l] = ls[l], ls[r]
    return l

def quickSort(ls, l, r):
    if l > r:
       return 
    po = partition(ls, l, r)
    #the input is the full array each time
    quickSort(ls, l, po-1)
    quickSort(ls, po+1, r)

ls = [1, 5, 3, 7, 4, 10, 9, 12]
quickSort(ls, 0, len(ls)-1)
print ls


