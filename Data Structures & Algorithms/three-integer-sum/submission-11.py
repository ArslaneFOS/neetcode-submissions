class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            return []

        nums.sort()
        results = []
        a : int | None = None
        for i in range(len(nums)):
            if nums[i] == a:
                continue
            a = nums[i]
            if a > 0: 
                break

            l, r = i + 1, len(nums) - 1
            while l < r:
                curSum = a + nums[l] + nums[r]
                if curSum < 0:
                    l += 1
                elif curSum > 0:
                    r -= 1
                else:
                    results.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
                        
        
        return results