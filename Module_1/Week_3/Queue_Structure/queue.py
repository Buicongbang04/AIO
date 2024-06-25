from node import Node

class Queue:
  def __init__(self, capacity) -> None:
    self.capacity = capacity
    self.front_p = None
    self.rear_p = None
    self.size = 0
    
  
  def is_empty(self):
    return True if self.size == 0 else False
  
  def is_full(self):
    return True if self.size == self.capacity else False
  
  def dequeue(self):
    if self.is_empty():
      print("Queue have no value")
      return
    
    res = self.front_p
    self.front_p = self.front_p.next
    self.size -= 1
    res.next = None
    
    if self.is_empty():
      self.front_p = None
      self.rear_p = None
    
    return res.data
  
  def enqueue(self, value):
    new_node = Node(value)

    if self.is_empty():
      self.front_p = new_node
      self.rear_p = new_node
    else:
      self.rear_p.next = new_node
      self.rear_p = new_node
    
    self.size += 1
    
    print(f'Add {value} to queue successfully!')
    return True
    
  def front(self):
    return self.front_p.data