class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
            if total > target or i >= len(nums):
                return

            # add cur num choice
            subset.append(nums[i])
            dfs(i, total + nums[i])

            # not add cur num choice
            subset.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return res