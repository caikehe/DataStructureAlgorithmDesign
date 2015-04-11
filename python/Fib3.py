#!/usr/bin/env python

import time

def fib_recursion(n):
    if n < 2:
        return n
    else:
        return fib_recursion(n-1)+fib_recursion(n-2)


def fib_iteration(n):
    a, b = 0, 1
    for i in xrange(n-1):
        a, b = b, a+b
    return b

known = {0:0, 1:1}
def fib_dictionary(n):
    if n not in known:
        known[n] = fib_dictionary(n-1)+fib_dictionary(n-2)
    return known[n]

n = 40   
t0 = time.clock()
print fib_recursion(n)
t1 = time.clock()
print "time elapse " + str(t1-t0)

t0 = time.clock()
print fib_iteration(n)
t1 = time.clock()
print "time elapse " + str(t1-t0)

t0 = time.clock()
print fib_dictionary(n)
t1 = time.clock()
print "time elapse " + str(t1-t0)


