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
    
  def insert_before_node(self, prev_node, node):
    new_node = DoubleNode(node)

    if not prev_node:
      print("Previous node doesn't exist!")
      return
    
    if prev_node.prev is None:
      new_node.next = prev_node
      prev_node.prev = new_node
      self.head = new_node
      return

    prev_node.prev.next = new_node
    new_node.next = prev_node
    
    
  def insert_after_node(self, prev_node, node):
    new_node = DoubleNode(node)

    if not prev_node:
      print("Previous node doesn't exist!")
      return

    new_node.next = prev_node.next
    prev_node.next = new_node




  def printList(self):
    cur = self.head

    while cur:
      print(cur.data)
      cur = cur.next