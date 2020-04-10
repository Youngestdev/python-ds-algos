from Nodes import DoubleNode

class DoubleLinkedList:
  """
  Implementation for Double Linked List
  """

  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = DoubleNode(data)
    cur = self.head

    if not self.head:
      self.head = new_node
      return
    
    while cur and cur.next != None:
      cur.prev = cur
      cur = cur.next
    new_node.prev = cur
    cur.next = new_node
    new_node.next = None

  def prepend(self, data):
    new_node = DoubleNode(data)
    cur = self.head

    if not self.head:
      self.head = new_node
      return
  
    cur.prev = new_node      
    new_node.next = cur  
    self.head = new_node
    

  def printList(self):
    cur = self.head

    while cur:
      print(cur.data)
      cur = cur.next