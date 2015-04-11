#!/usr/bin/env python 

def AnAnagramDetection(s1, s2):
    s3 = list(s1)
    s4 = list(s2)
    len1 = len(s3)
    len2 = len(s4)
    if len1!=len2:
        return False
    for i in range(len1):
        if s1.find(s4[i])==-1 or s2.find(s3[i])==-1:
            return False
    return True


s1 = "heart1"
s2 = "earth"
print AnAnagramDetection(s1,s2)
      
