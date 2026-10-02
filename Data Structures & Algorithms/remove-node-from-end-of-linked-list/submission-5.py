# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        left, right = dummy, head

        count = 1

        while right and right.next:
            if count >= n:
                left = left.next
                print(left.val)

            right = right.next
            count += 1

        left.next = left.next.next
        
        return dummy.next