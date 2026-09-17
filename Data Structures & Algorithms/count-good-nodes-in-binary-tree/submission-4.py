# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode | None, prevMax: int = -101) -> int:
            if not node: return 0
            print(prevMax)
            if node.val < prevMax:
                return 0 + dfs(node.left, max(node.val, prevMax)) + dfs(node.right, max(node.val, prevMax))

            else:
                return 1 + dfs(node.left, max(node.val, prevMax)) + dfs(node.right, max(node.val, prevMax))

        return dfs(root)