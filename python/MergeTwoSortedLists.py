#!/usr/bin/env python 

def merge(sorted_list1, sorted_list2):
    result = []
    len1 = len(sorted_list1)
    len2 = len(sorted_list2)
    index1 = 0
    index2 = 0
    while True:
        # list1 has finished, add remaining items from sorted_list2
        if index1 >= len1:
            result.extend(sorted_list2[index2:])
            return result
        if index2 >= len2:
            result.extend(sorted_list1[index1:])
            return result
        # both lists have items, copy smaller one to result
        if sorted_list1[index1] < sorted_list2[index2]:
            result.append(sorted_list1[index1])
            index1 += 1
        else:
            result.append(sorted_list2[index2])
            index2 += 1
  

list1 = [1,3,5,7,9,11,13,15,17,19]
list2 = [4,8,12,16,20,24]
print merge(list1, list2)
