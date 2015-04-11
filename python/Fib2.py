#!/usr/bin/env python 

def fib(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

f1000 =  fib(1000)
print f1000
