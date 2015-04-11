#!/usr/bin/env python 
 
alreadyknow = {0:0, 1:1}
def fib(n):
    if n not in alreadyknow:
        alreadyknow[n] = fib(n-1) + fib(n-2)
    return alreadyknow[n]

print fib(100)
