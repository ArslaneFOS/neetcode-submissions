# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        N : int = 0
        node = head
        while node:
            node = node.next
            N += 1

        node = head
        prev = None

        for i in range(N - n):
            prev = node
            node = node.next

        if prev:
            prev.next = node.next
        else:
            head = node.next or None

        return head