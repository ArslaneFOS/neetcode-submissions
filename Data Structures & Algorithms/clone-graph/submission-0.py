"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copyMap : dict = {}

        def dfs1(node: Optional[Node]) -> None:
            nonlocal copyMap

            if not node:
                return

            if node not in copyMap:
                copyMap[node] = Node(node.val, [])

                for n in node.neighbors:
                    dfs1(n)

        def dfs2(node: Optional[Node]) -> None:
            nonlocal copyMap

            if not node:
                return

            copy = copyMap[node]
            if copy.neighbors:
                return

            for n in node.neighbors:
                copy.neighbors.append(copyMap[n])
                dfs2(n)
            

        dfs1(node)
        dfs2(node)

        return copyMap[node] if copyMap else None
        
