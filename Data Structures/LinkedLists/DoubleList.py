from Nodes import DoubleNode


class DoubleLinkedList:
    """
    Implementation for Double Linked List
    """

    def __init__(self):
        self.head = None

    def __len__(self):
        count = 0
        cur = self.head

        while cur:
            count += 1
            cur = cur.next
        return count

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

    def delete_node(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                if not cur.next:
                    self.head = None
                    return

                else:
                    next_node = cur.next
                    cur = None  # This should set the entire node's data to None, yeah?
                    cur = next_node
                    self.head = cur
                    return
            elif cur.data == key:
                if cur.next:
                    cur.prev.next = cur.next
                    cur = None
                    return
                else:
                    cur.prev.next = None
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def reverse(self):
        cur = self.head
        prev_node = None

        if len(self) == 1:
            return self.head

        while cur:
            prev_node = cur.prev
            cur.prev = cur.next
            cur.next = prev_node
            cur = cur.prev
        if prev_node:
            self.head = prev_node.prev

    def printlist(self):
        cur = self.head

        while cur:
            print(cur.data, end="->")
            cur = cur.next
