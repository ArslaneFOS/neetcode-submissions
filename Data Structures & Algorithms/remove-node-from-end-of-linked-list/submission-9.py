# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        dummy = ListNode(next=node)

        prev = dummy

        while node and node.next:
            if n <= 1:
                prev = prev.next

            node = node.next
            n -= 1

        prev.next = prev.next.next

        return dummy.next

        