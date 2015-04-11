class Queue():
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    #return the first element in the queue
    def dequeue(self):
        return self.items.pop(0)
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)


class Deque():
    def __init__(self):
        self.items = []
    #insert element at the first position
    def enqueue_front(self, item):
        self.items.insert(0, item)
    def enqueue_end(self, item):
        self.items.append(item)
    def dequeue_front(self):
        return self.items.pop(0)
    def dequeue_end(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.items == []

def palindrome(s):
    deque = Deque()
    for i in s:
        deque.enqueue_end(i)
    while not deque.is_empty() and deque.size() > 1:
        if deque.dequeue_front() != deque.dequeue_end():
            return False 
    return True

s1 = "lsdkjfskf"
s2 = "radar"
print(palindrome(s1))
print(palindrome(s2))
