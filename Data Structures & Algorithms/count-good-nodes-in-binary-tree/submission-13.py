# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode | None, prevMax) -> int:
            if not node: return 0

            res = 1 if node.val >= prevMax else 0
            prevMax = max(node.val, prevMax)
            res += dfs(node.left, max(node.val, prevMax))
            res += dfs(node.right, max(node.val, prevMax))
            return res


        return dfs(root, root.val)