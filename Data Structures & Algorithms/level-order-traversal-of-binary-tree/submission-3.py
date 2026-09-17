# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        cur_level = 0

        res = []

        if not root: return res

        q.append(root)

        while q:
            res.append([])
            len_q = len(q)
            for _ in range(len_q):
                node = q.popleft()

                res[cur_level].append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            cur_level += 1

        return res
