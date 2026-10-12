class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        digitToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def dfs(i, cur: str):
            if i >= len(digits):
                res.append(str(cur))
                return

            for c in digitToLetters[digits[i]]:
                cur += c
                dfs(i + 1, cur)
                cur = cur[:-1]

        dfs(0, "")

        return res