# LinkedList implementation!!

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node

  def prepend(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_after_node(self, prev_node, data):
    new_node = Node(data)
    if not prev_node:
      print("Previous mode doesn't exist")
      return

    new_node.next = prev_node.next
    prev_node.next = new_node

  def printList(self):
    cur_node = self.head
    while cur_node:
      print(cur_node.data)
      cur_node = cur_node.next

aList = LinkedList()
aList.append("Tomatoes")
aList.append("Pepper")
aList.prepend("Money")
aList.insert_after_node(aList.head.next, "Idk")
aList.printList()