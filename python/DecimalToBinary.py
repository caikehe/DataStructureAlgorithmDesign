class Stack():
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, ele):
        self.items.append(ele)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

def Decimal2Base(v, base):
    stack = Stack()
    num = "0123456789abcdef"
    while v:
        stack.push(num[v%base])
        v /= base
    result = ""
    while not stack.is_empty():
        result += str(stack.pop())
    return result

v = 255
print Decimal2Base(v, 2)
print Decimal2Base(v, 16)
