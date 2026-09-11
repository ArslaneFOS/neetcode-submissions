class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)

        
        char_dict : dict = {}

        max_length = 0
        left = 0
        for i, c in enumerate(s):
            if c in char_dict:
                left = max(left, char_dict[c] + 1)
            char_dict[c] = i
            max_length = max(max_length, i - left + 1)

        return max_length