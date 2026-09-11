class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        mid = low + (high - low)//2

        while nums[low] > nums[mid] or nums[mid] > nums[high]:
            if nums[mid] <= nums[low] and nums[mid] < nums[high]:
                val = nums.pop(0)
                nums.append(val)
            elif nums[mid] >= nums[low] and nums[mid] > nums[high]:
                val = nums.pop()
                nums.insert(0, val)

        return nums[low]