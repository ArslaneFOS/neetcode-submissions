class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        water = 0

        maxL, maxR = 0, 0

        while l < r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])

            if maxR > maxL:
                l += 1
                if l < r: 
                    water += maxL - height[l] if maxL >= height[l] else 0
            else:
                r -= 1
                if r > l: 
                    water += maxR - height[r] if maxR >= height[r] else 0

        return water