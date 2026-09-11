class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        mp1 = {}

        for c in s1:
            mp1[c] = mp1.get(c, 0) + 1

        mp2 = {}
        l = 0
        for r in range(len(s2)):          
            mp2[s2[r]] = mp2.get(s2[r], 0) + 1
            if r - l + 1 > len(s1):
                if s2[l] in mp2:
                    if mp2[s2[l]] == 1:
                        mp2.pop(s2[l])
                    else:
                        mp2[s2[l]] -= 1
                l += 1

            if mp1 == mp2:
                return True
            
        return False