class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = [1] # right to left
        p = [1] # left to right

        # build prefix:
        for i in range(len(nums)-1):
            p.append(p[i]*nums[i])

        for i in range(len(nums)-1, 0, -1):
            s.append(s[len(nums)-1-i]*nums[i])
        s.reverse()

        results = []
        for pi, si in zip(p,s):
            results.append(pi*si)

        return results

        