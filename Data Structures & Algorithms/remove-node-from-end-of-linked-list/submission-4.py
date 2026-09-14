# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy, node = ListNode(), head
        dummy.next = node

        count = 0
        prev_to_delete = dummy
        to_delete = head
        while node:
            if count >= n:
                prev_to_delete = to_delete
                to_delete = to_delete.next
            node = node.next
            count += 1

        prev_to_delete.next = to_delete.next

        return dummy.next
        