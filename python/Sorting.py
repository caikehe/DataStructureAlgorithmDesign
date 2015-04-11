#!/usr/bin/env python 

# 6 Stable sorts
def bubbleSort(ls):
    for i in xrange(len(ls), 0, -1):
        for j in xrange(1, i):
            if ls[j] < ls[j-1]:
                 ls[j], ls[j-1] = ls[j-1], ls[j]
    return ls

def insertionSort(ls):
    for i in xrange(1, len(ls)):
        tmp = ls[i]
        for j in xrange(i-1, -1, -1):
            if ls[j] > ls[i]:
                ls[j+1] = ls[j]
            else:
                if j != i-1:
                    ls[j] = tmp
                break
    return ls 

#buck is in a range, usually it takes large space
#and has no duplication
def bucketSort(ls):
    bucket = [-1]*(max(ls)-min(ls)+1)
    for item in ls:
        bucket[item] = item
    start = 0
    for item in bucket:
        if item != -1:
            ls[start] = item
            start += 1

def countingSort(ls):
    pass

#merge two sorted lists
def merge(ls1, ls2):
    res = []
    i = 0; j = 0
    while i < len(ls1) and j < len(ls2):
        if ls1[i] > ls2[j]:
            res.append(ls2[j])
            j += 1
        else:
            res.append(ls1[i])
            i += 1
    if i < len(ls1):
        res.extend(ls1[i:])
    if j < len(ls2):
        res.extend(ls2[j:])
    return res
#is not sorted in place, has return value
def mergeSort(ls):
    mid = len(ls)/2
    if mid < 1:
        return ls
    left = mergeSort(ls[:mid])
    right = mergeSort(ls[mid:])
    return merge(left, right)

def binaryTreeSort(ls):
    pass

def radixSort(ls):
    pass

# 4 Unstable sorts
def selectionSort(ls):
    for i in xrange(len(ls)):
        mini = ls[i]
        for j in xrange(i+1, len(ls)):
            if ls[j] < mini:
                mini = ls[j]
        ls[i] = mini
    return ls

def shellSort(ls):
    pass

def heapSort(ls):
    pass

#quickSort is inplace, no return value
def quickSort(ls, l, h):
    if l < h:
        pos = partition(ls, l, h) 
        #input the full array to recursive function
        quickSort(ls, l, pos-1)
        quickSort(ls, pos+1, h)

def partition(ls, l, h):
    pivot = ls[h]
    for i in xrange(l, h):
        if ls[i] < pivot:
            ls[l], ls[i] = ls[i], ls[l]
            l += 1
    #now l records the position for pivot, exchange
    ls[l], ls[h] = ls[h], ls[l]
    return l

array = [1, 4, 0, 3, 9, 11, 2, 5, 8]
#newArray1 = bubbleSort(array)
#newArray2 = insertionSort(array)
#newArray3 = selectionSort(array)
#quickSort(array, 0, len(array)-1);print array
#newArray4 = bucketSort(array); print newArray4
newArray5 = mergeSort(array); print newArray5
