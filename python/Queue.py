class Node:
    def __init__(self, cargo):
        self.cargo = cargo
        self.next = None

class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0
 
    def insert(self, cargo):
        node = Node(cargo)
        # if list is empty the new node goes first
        if self.head is None:
            self.head = node
        else:
            # find the last node in the list
            last = self.head
            while last.next:
                last = last.next
            last.next = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        return cargo

q = Queue()
for num in [11, 12, 14, 13]:
    q.insert(num)

while not q.is_empty():
    print(q.remove())
print("")

class ImprovedQueue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None
    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.length == 0:
            self.head = self.last = node
        else:
            last = self.last 
            # append the last node
            last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo

q = ImprovedQueue()
for num in [11, 12, 14, 13]:
    q.insert(num)

while not q.is_empty():
    print(q.remove())
print

class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)
    
    def remove(self):
        maxi = 0
        for i in xrange(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item

q = PriorityQueue()
for num in [11, 12, 14, 13]:
    q.insert(num)

while not q.is_empty():
    print(q.remove())

class Golfer:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __str__(self):
        return "{0:16}: {1}".format(self.name, self.score)

    def __gt__(self, other):
        return self.score < other.score # less is more

print("")
tiger = Golfer("Tiger Woods", 61)
phil = Golfer("Phil Mickelson", 72)
hal = Golfer("Hal Sutton", 69)
pq = PriorityQueue()
for g in [tiger, phil, hal]:
    pq.insert(g)

while not pq.is_empty():
    print(pq.remove())





 







  
