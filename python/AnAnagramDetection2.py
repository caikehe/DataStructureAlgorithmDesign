#!/usr/bin/env python 

def AnAnagramDetection(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1!=len2:
        return False
    for i in range(len1):
        if s1.find(s2[i])==-1 or s2.find(s1[i])==-1:
            return False
    return True

def AnAnagramDetection1(s1, s2):
    l1 = list(s1)
    l2 = list(s2)
    l1.sort()
    l2.sort()
    #return l1 == l2
    for i in xrange(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True

# check off
def AnAnagramDetection2(s1, s2):
    ls = list(s2)
    for i in xrange(len(ls)):
        for w in ls:
            if s1[i] == w:
                ls.remove(w)
                continue
    return len(ls)==0
    
# count and compare
def AnAnagramDetection3(s1, s2):
    c1 = [0]*26
    c2 = [0]*26
    for i in xrange(len(s1)):
        c1[ord(s1[i])-ord('a')] += 1

    for i in xrange(len(s1)):
        c2[ord(s2[i])-ord('a')] += 1

    for i in xrange(26):
        #print c1[i], c2[i]
        if c1[i] != c2[i]:
            return False
    return True

d1 = {}
d2 = {}
def AnAnagramDetection4(s1, s2):
    for i in s1:
        d1[i] = d1.get(i, 0) + 1

    for i in s2:
        d2[i] = d2.get(i, 0) + 1
    return d1 == d2
    '''  
    for i in d1.keys():
        print i, d1[i], d2[i]
        if d1[i] != d2[i]:
            return False
    return True
    '''

s1 = "hhearte"
s2 = "earteh"
print AnAnagramDetection4(s1,s2)
      
