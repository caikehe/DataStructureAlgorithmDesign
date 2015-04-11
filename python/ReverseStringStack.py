#!/usr/bin/env python 

class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def push(self, ele):
        self.items.append(ele)

    def peep(self):
        return self.items[len(self.items)-1]


def ReverseString(s):
    stack = Stack()
    for elem in s:
        stack.push(elem)
    result = []
    while not stack.is_empty():
       result.append(stack.pop())
    return result

s = "caikehe"
print ReverseString(s)
    
