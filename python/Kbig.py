#!/usr/bin/env python 

def Kbig(ls, k):
    if k <= 0:
        return []
    if len(ls) <= k:
        return ls
    #subscript is po, start from 0
    po = Partition(ls, 0, len(ls)-1)
    print po
    return Kbig(ls[0:po], k).extend(Kbig(ls[po:], k-po+1))

def Partition(ls, l, h):
    pivot = ls[h]
    for i in xrange(l, h):
        if ls[i] <  pivot:
            ls[i], ls[l] = ls[l], ls[i]
            l += 1
    #put pivot in the right position
    ls[l], ls[h] = ls[h], ls[l]
    return l

ls = [1, 5, 7, 11, 23, 25, 56, 89]
print Kbig(ls, 3)
