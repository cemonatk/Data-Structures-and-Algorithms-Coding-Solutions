#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data=None, next=None): 
    self.data = data
    self.next = next
  
class LinkedList:
    def __init__(self, head=None):
        self.head = None
    
    # insertion method for the linked list
    def insert(self, data):
        

    # print method for the linked list
    def listprint(self):
        pass

# Creating a single node
test = SLinkedList()
first = Node(3)
list.headval = Node("Mon")
print(first.data)