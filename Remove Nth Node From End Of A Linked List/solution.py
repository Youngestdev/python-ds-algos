# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 0
        # length = self.len_iterative(head)
        distance_from_end = (self.len_iterative(head) - n)
        cur = head
        prev = None

        if n == self.len_iterative(head) and self.len_iterative(head) == 1:
            head = None
            return head

        if distance_from_end <= 0:
            # nxt = head.next
            # head = None
            head = head.next
            return head

        while count != distance_from_end:
            count += 1
            prev = head
            head = head.next
        prev.next = head.next
        head = None

        return cur

    def len_iterative(self, head: ListNode):
        count = 0
        while head is not None:
            count += 1
            head = head.next
        return count
