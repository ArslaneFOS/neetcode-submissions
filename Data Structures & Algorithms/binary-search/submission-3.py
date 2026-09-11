class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low<=high:
            m = low + (high - low)//2

            if nums[m] < target:
                low = m + 1
            elif nums[m] > target:
                high = m - 1
            else:
                return m
        return -1
        