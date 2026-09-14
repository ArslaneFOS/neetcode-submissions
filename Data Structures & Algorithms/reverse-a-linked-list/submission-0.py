# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curNode = head
        nextNode = curNode.next if curNode else None
        prevNode = None
        while curNode:
            nextNode = curNode.next if curNode else None
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode

        return prevNode



            