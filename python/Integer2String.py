#!/usr/bin/env python 
def integerToString(num, base):
    st = "0123456789abcdef"
    if num < base:
        return st[num]
    else:
        return integerToString(num//base, base) + st[num%base]

print(integerToString(1453, 16))
