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

  def delete(self, key):
    cur_node = self.head
    if cur_node and cur_node.data == key:
      self.head = cur_node.next
      # set previous node to none
      cur_node = None
      return

    Prev = None
    while cur_node and cur_node.data != key:
      Prev = cur_node
      cur_node = cur_node.next

      if cur_node is None:
        return
      
      Prev.next = cur_node.next
      cur_node = None

  def delete_by_pos(self, pos):
    cur_node = self.head

    if pos == 0:
      self.head = cur_node.next
      cur_node = None

    Prev = None
    count = 0
    
    while cur_node and count != pos:
      Prev = cur_node
      cur_node = cur_node.next
      count += 1

      if cur_node is None:
        return

      Prev.next = cur_node.next
      cur_node = None

  def len_iterative(self):
    count = 0
    cur_node = self.head

    while cur_node:
      count += 1
      cur_node = cur_node.next
    return count

  def len_recursive(self, node):
    if node is None:
      return 0
    return 1 + self.len_recursive(node.next)

  def node_swap(self, key_1, key_2):
    prev_1 = None
    curr_1 = self.head

    while curr_1 and curr_1.data != key_1:
      prev_1 = curr_1
      curr_1 = curr_1.next

    prev_2 = None
    curr_2 = self.head

    while curr_2 and curr_2.data != key_2:
      prev_2 = curr_2
      curr_2 = curr_2.next

    if prev_1:
      prev_1.next = curr_2
    else:
      self.head = curr_2

    if prev_2:
      prev_2.next = curr_1
    else:
      self.head = curr_1
    
    curr_1.next, curr_2.next = curr_2.next, curr_1.next

      

aList = LinkedList()
aList.append("Tomatoes")
aList.append("Pepper")
aList.prepend("Money")
aList.insert_after_node(aList.head.next, "Idk")
aList.node_swap("Idk", "Pepper")
aList.printList()