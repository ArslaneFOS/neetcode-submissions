# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = ListNode()
        dummy.next = node

        r = 0
        while l1 or l2:
            val = 0
            if l1 and l2:
                val = l1.val + l2.val
            elif l1:
                val = l1.val
            elif l2:
                val = l2.val
            val += r
            node.val = val % 10

            r = (val - (val % 10))//10
            if (l1 and l1.next) or (l2 and l2.next):
                node.next = ListNode()
                node = node.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if r > 0:
            node.next = ListNode(r, None)

        return dummy.next