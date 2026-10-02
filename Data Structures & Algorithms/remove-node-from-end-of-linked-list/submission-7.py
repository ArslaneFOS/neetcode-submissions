# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        left, right = dummy, head

        while right and right.next:
            right = right.next
            n -= 1
            
            if n < 1:
                left = left.next

        left.next = left.next.next
        
        return dummy.next