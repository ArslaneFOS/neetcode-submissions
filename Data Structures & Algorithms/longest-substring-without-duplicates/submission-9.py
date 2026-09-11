class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)

        
        mp : dict = {}

        l = 0
        res = 0

        for i, c in enumerate(s):
            if c in mp:
                l = max(l, mp[c] + 1)
            mp[c] = i
            res = max(res, i - l + 1)
        return res