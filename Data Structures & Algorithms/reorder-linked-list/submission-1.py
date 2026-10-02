# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return


        # cut list in half
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondHalf = slow.next
        slow.next = None

        # reverse second half list
        curNode = secondHalf
        prevNode = None

        while curNode:
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
        
        revHalf = prevNode

        # insertion
        first, second = head, revHalf
        while second:
            firstNext, secondNext = first.next, second.next

            first.next = second
            second.next = firstNext

            first, second = firstNext, secondNext

