class Solution:
    def trap(self, height: List[int]) -> int:
        total : int = 0

        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]

        while r > l:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                total += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                total += maxRight - height[r]

        return total