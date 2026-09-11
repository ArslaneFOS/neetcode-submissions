class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea : int = 0
        while l < r:
            area = (r - l) * min(heights[r], heights[l])

            maxArea = max(maxArea, area)

            if heights[r] <= heights[l]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
                
        return maxArea