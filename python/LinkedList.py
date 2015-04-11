#!/usr/bin/env python 

from __future__ import print_function

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)
     
    def print_backward(self):
        if self.next is not None:
            tail = self.next
            tail.print_backward()
        print(self.cargo, end = " ")

def print_list(node):
    while node is not None:
        print(node, end = " ")
        node = node.next
    print()

def print_backward(lst):
    if lst is None: return 
    head = lst
    tail = lst.next
    print_backward(tail)
    print(head, end=" ")
    
def remove_second(lst):
    if lst is None: return 
    first = lst
    second = lst.next
    first.next = second.next
    second.next = None 
    return second

def print_backward_nicely(lst):
    if lst is None: return 
    print("[", end = " ")
    print_backward_nicely(lst.next)
    print(lst, end = " ]")

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None 

    def print_backward(self):
        print("[", end = " ")
        if self.head is not None:
            self.head.print_backward()

    def add_first(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

print_list(node1)
print_backward(node1)
print()
print_backward_nicely(node1)
print()
print(remove_second(node1))
print_list(node1)


