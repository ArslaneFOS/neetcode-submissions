"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        originalNode = head
        copyNode = Node(0)

        og_co_map = {}

        while originalNode:
            copyNode.val = originalNode.val
            copyNode.next = Node(0) if originalNode.next else None
            og_co_map[originalNode] = copyNode

            copyNode = copyNode.next
            originalNode = originalNode.next

        
        originalNode = head

        while originalNode:
            randomOriginal = originalNode.random
            if randomOriginal: og_co_map[originalNode].random = og_co_map[randomOriginal]
            originalNode = originalNode.next

        return og_co_map[head]




