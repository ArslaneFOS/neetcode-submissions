class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(0, nums)
        return self.res
    
    def dfs(self, idx, nums):
        if idx == len(nums) - 1:
            self.res.append(list(nums))
            return
        
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.dfs(idx + 1, nums)
            nums[idx], nums[i] = nums[i], nums[idx]

