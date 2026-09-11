class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in nums_dict:
                return [nums_dict[difference], i]
            else:
                nums_dict[nums[i]] = i