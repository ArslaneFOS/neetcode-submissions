class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l)//2

            if nums[m] == t:
                return m

            if nums[m] > nums[r]:
                if (nums[m] > t and nums[r] >= t) or (nums[m] < t and nums[r] <= t):
                    l = m + 1
                else:
                    r = m - 1
            else:
                if (nums[m] > t and nums[r] >= t) or (nums[m] < t and nums[r] < t):
                    r = m - 1
                else:
                    l = m + 1

        return -1