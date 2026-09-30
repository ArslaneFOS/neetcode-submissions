class Solution:
    def search(self, nums: List[int], t: int) -> int:
        # [1,2,3,4,5]
        # [2,3,4,5,1]
        # [3,4,5,1,2]
        # [4,5,1,2,3]
        # [5,1,2,3,4]

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r + l) // 2

            if nums[mid] == t:
                return mid

            if nums[mid] >= nums[l]:
                if t < nums[l] or t > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if t > nums[r] or t < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1