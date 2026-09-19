# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(
            node: Optional[TreeNode], low: float = float("-inf"), high: float = float("inf")
        ):
            if not node:
                return True

            if not (low < node.val < high):
                return False

            left_is_valid = validate(node.left, low=low, high=node.val)
            right_is_valid = validate(node.right, low=node.val, high=high)

            return left_is_valid and right_is_valid

        return validate(root)
