from __future__ import print_function

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
 
    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

'''
s = Stack()
s.push(3)
s.push(30)
s.push("+")

while not s.is_empty():
    print(s.pop(), end = " ")

print()
'''
'''
def eval_postfix(ex):
    import re
    token_list = re.split("([^0-9])", ex)
    stack = Stack()
    for token in token_list:
        if token == "" or token == " ":
            continue
        if token == "+":
            sum = stack.pop() + stack.pop()
            stack.push(sum)
        elif token == "*":
            product = stack.pop() * stack.pop()
            stack.push(product)
        else:
            stack.push(int(token))
    return stack.pop()

print(eval_postfix("56 47 + 2 *"))    
'''




