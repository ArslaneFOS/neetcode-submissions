"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return None

        root = node
        oldToCopy = defaultdict(lambda: Node())

        q = collections.deque([node])

        while q:
            cur = q.popleft()
            copy = oldToCopy[cur]
            copy.val = cur.val
            for child in cur.neighbors:
                if child not in oldToCopy:
                    q.append(child)
                copy.neighbors.append(oldToCopy[child])


        return oldToCopy[root]