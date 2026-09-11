class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        close_to_open = {"}": "{", ")": "(", "]": "["}
        stack = []

        for c in s:
            if c not in close_to_open:
                stack.append(c)
                continue
            if len(stack) > 0:
                if stack[-1] == close_to_open[c]:
                    stack.pop()
                    continue
            stack.append(c)

        return len(stack) == 0