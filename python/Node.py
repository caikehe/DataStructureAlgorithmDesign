class Node():
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, newnext):
        self.next = newnext

class UnorderedList():
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self, item):
        tmp = Node(item)
        tmp.setNext(self.head)
        self.head = tmp
    def size(self):
        s = 0
        while self.head != None:
            count += 1
            self.head = self.head.getNext()
        return s
    def search(self, item):
        index = 0
        while self.head != None:
            if self.head.getData() == item:
                return index
            self.head  = self.head.getNext()
            index += 1
        return False
    #should have at least 1 elements
    def remove(self, item):
        current = self.head
        pre = None
        while current != None:
            if current.getData() != item:
                pre = current
                current = current.getNext()
            elif pre == None:
                self.head = current.getNext()
            else:
                pre.setNext(current.getNext())
            
    def append(self, item):
    def insert(self, item):
    def index(self, item);
    def pop(self, item):

class OrderedList():
    def __init__(self):
    def add(self, item):
    def remove(self, item):
    def search(self, item):
    def isEmpty(self):
    def size():
    def index(self, item):
    def pop(self):
    def pop(self, pos):




















	
