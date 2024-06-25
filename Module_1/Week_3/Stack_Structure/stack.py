from node import Node

class Stack:
  def __init__(self, capacity:int):
    self.capacity = capacity
    self.head = 0
    self.size = 0
        
  def is_empty(self):
    return True if self.size == 0 else False
  
  def is_full(self):
    return True if self.size == self.capacity else False
  
  def push(self, value:int):
    if (self.is_full()):
      print("Stack is full")
      return
    
    new_node = Node(value)
    if self.size == 0:
      self.head = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    self.size += 1
    
  def pop(self):
    if (self.is_empty()):
      print("Stack is empty")
      return
    
    temp = self.head
    self.head = self.head.next
    temp.next = None
    self.size -= 1
    return temp.data
  
  def top(self):
    if (self.is_empty()):
      print("Stack is empty")
      return
    return self.head.data

  