#!/usr/bin/env python 

class Stack():
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, ele):
        self.items.append(ele)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def BalancedParentheses(s):
    stack = Stack()
    for ele in s:
        if ele == "(":
            stack.push(ele)
        elif ele == ")":
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

def BalancedGeneral(s):
    stack = Stack()
    for e in s:
        if e in "([{":
            stack.push(e)
        else:
            if stack.is_empty():
                return False
            if not match(stack.pop(), e):
                return False
    return stack.is_empty()


def match(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)
 
#s = "(()((())()))"
#s = "(()()(()"
#print BalancedParentheses(s)
s = '{{([][])}()}'
#s = '[{()]'
print BalancedGeneral(s)

