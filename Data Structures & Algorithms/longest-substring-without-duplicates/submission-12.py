class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        mp = {} # "c" -> index
        l = 0
        res = 0

        for i, c in enumerate(s):
            if c in mp:
                l = max(mp[c] + 1, l) # either it was seen before l, therefore we don't care and the index will be updated, or it is within the window, so we jump l to the character right after
            mp[c] = i
            res = max(res, i - l + 1)

        return res