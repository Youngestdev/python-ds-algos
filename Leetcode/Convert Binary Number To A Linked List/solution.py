# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = str
        arr = ""
        while head is not None:
            arr += s(head.val)
            head = head.next
        return int(arr, base=2)

