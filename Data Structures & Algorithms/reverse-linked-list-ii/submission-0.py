# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        leftNode = dummy

        for _ in range(left - 1):
            leftNode = leftNode.next

        prev = None
        sublist = leftNode.next

        for _ in range(right - left + 1):
            nextNode = sublist.next
            sublist.next = prev
            prev = sublist
            sublist = nextNode
        
        tail = leftNode.next
        leftNode.next = prev
        tail.next = sublist

        return dummy.next