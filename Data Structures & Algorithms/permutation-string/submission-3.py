class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp1 = {}

        for c in s1:
            mp1[c] = mp1.get(c, 0) + 1

        l = 0
        for r in range(len(s1)-1, len(s2)):
            mp2 = {}
            for c in s2[l:r+1]:
                mp2[c] = mp2.get(c, 0) + 1

            if mp1 == mp2:
                return True
            
            l += 1
        return False