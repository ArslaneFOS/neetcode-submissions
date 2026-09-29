class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums) # O(n)

        maxLen = 0

        for n in nums:                
            if (n - 1) not in numsSet:
                length = 1
                while n + length in numsSet:
                    length += 1
                
                maxLen = max(maxLen, length)

        return maxLen