from Nodes import Node

class CircularLinkedList:
  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = Node(data)
    cur_node = self.head


    if not self.head:
      self.head = new_node
      new_node.next = self.head # Idk, I can also set this to new_node abi?
      return
    
    while cur_node.next != self.head:
      cur_node = cur_node.next
    cur_node.next = new_node
    new_node.next = self.head

  def prepend(self, data):
    cur = self.head
    new_node = Node(data)
    new_node.next = self.head

    if not self.head:
      new_node.next = new_node
    else:        
      while cur.next != self.head:
        cur = cur.next
      cur.next = new_node
    self.head = new_node

  def remove(self, key):
    if self.head:
      if self.head.data == key:
        cur = self.head
        while cur.next != self.head:
          cur = cur.next
        if self.head == self.head.next:
          self.head = None
        else:
          cur.next = self.head.next
          self.head = self.head.next
      else:
        cur = self.head
        prev = None
        while cur.next != self.head:
          prev = cur
          cur = cur.next
          if cur.data == key:
            prev.next = cur.next
            cur = cur.next

  def printList(self):
    cur = self.head

    while cur:
      print(cur.data)
      cur = cur.next

      if cur == self.head:
        return
      

  def __len__(self):
    cur = self.head
    count = 0

    while cur:
      count += 1
      cur = cur.next

      if cur == self.head:
        break
    
    return count

  def split_list(self):
    size = len(self)

    if size == 0:
      return None
    if size == 1:
      return self.head

    mid = size // 2
    count = 0

    prev = None
    cur = self.head

    while cur and count < mid:
      count += 1
      prev = cur
      cur = cur.next
      # Once the loop breaks, set the last iterated node's ( not the current one) next pointer
      # to the head node.      
    prev.next = self.head

    splitted_list = CircularLinkedList()
    
    while cur.next != self.head:
      splitted_list.append(cur.data)
      cur = cur.next
      # What happends here? - Append the last node perhaps
    splitted_list.append(cur.data)

    self.printList()
    print("\n")
    splitted_list.printList()

  def remove_node(self, node):
    if self.head:
      if self.head == node:
        cur = self.head
        while cur.next != self.head:
          cur = cur.next
        if self.head == self.head.next:
          self.head = None
        else:
          cur.next = self.head.next
          self.head = self.head.next
      else:
        cur = self.head
        prev = None
        while cur.next != self.head:
          prev = cur
          cur = cur.next
          if cur == node:
            prev.next = cur.next
            cur = cur.next

  def josephus_circle(self, step):
    cur = self.head

    while len(self) > 1:
      count = 1
      while count != step:
        cur = cur.next
        count += 1
      print("KILL :" + str(cur.data))
      self.remove_node(cur)
      cur = cur.next