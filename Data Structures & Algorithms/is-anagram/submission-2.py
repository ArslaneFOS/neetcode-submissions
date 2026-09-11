class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {}
        t_dict = {}
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        
        for i in t:
            if i in t_dict:
                t_dict[i] += 1
            else:
                t_dict[i] = 1

        if s_dict == t_dict:
            return True
        return False