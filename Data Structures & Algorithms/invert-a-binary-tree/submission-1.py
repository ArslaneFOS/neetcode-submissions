# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root and not root.right and not root.left:
            return root

        if root and root.left and root.right:
            root.left, root.right = root.right, root.left

        elif root and root.left:
            root.left, root.right = None, root.left

        elif root and root.right:
            root.left, root.right = root.right, None
        
        if root and root.left:
            self.invertTree(root.left)

        if root and root.right:
            self.invertTree(root.right)

        return root


        