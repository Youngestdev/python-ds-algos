#!/usr/bin/python3
# Singly LinkedList implementation!!

from Nodes import Node


class LinkedList(object):
    def __init__(self, head):
        self.head = Node(head)

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

    def reverse(self):
        curr_node = self.head
        prev_node = None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node

    def merge_lists(self, list):
        p = self.head
        q = list.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = p.next
            else:
                s.next = q
                s = q
                q = q.next

        if not p:
            s.next = q
        if not q:
            s.next = p

        return new_head

    def remove_duplicates(self):
        cur = self.head
        prev = None
        duplicates = dict()

        while cur:
            if cur.data in duplicates:
                prev.next = cur.next
                cur = None
            else:
                duplicates[cur.data] = 1
                prev = cur
            cur = prev.next

    def nth_to_last_node(self, n):
        total_len = self.len_iterative()
        cur = self.head

        while cur:
            if total_len == n:
                print(cur.data)
                return cur.data
            total_len -= 1
            cur = cur.next

        if cur is None:
            return

    def count_occurences(self, data):
        count = 0
        cur = self.head

        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

            while p and count < k:
                prev = p
                p = p.next
                q = q.next
                count += 1
            p = prev

            while q:
                prev = q
                q = q.next
            q = prev

            q.next = self.head
            self.head = p.next
            p.next = None

    def isPalindrome_string(self):
        s = ""
        cur = self.head

        while cur:
            s += cur.data
            cur = cur.next
        return s == s[::-1]

    def isPalindrome_stack(self):
        s = []
        cur = self.head

        while cur:
            s.append(cur.data)
            cur = cur.next
        cur = self.head

        while cur:
            data = s.pop()
            if cur.data != data:
                return False
            cur = cur.next
        return True

    def move_tail_to_head(self):
        if self.head and self.head.next:
            last = self.head
            second_to_last = None
            while last.next:
                second_to_last = last
                last = last.next
            last.next = self.head
            second_to_last.next = None
            self.head = last

    def sum_of_two_lists(self, sList):
        p = self.head
        q = sList.head
        r = LinkedList()
        carry = 0

        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data

            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                r.append(remainder)
            else:
                carry = 0
                r.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        r.printList()

    def swap_adjacent_nodes(self):
        cur_node = self.head

        while cur_node and cur_node.next is not None:
            cur_node.data, cur_node.next.data = cur_node.next.data, cur_node.data
            cur_node = cur_node.next.next
