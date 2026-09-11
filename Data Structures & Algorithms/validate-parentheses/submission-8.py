class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        stack = []

        for c in s:
            if c == "{" or c == "(" or c == "[":
                stack.append(c)
                continue
            if len(stack) > 0:
                if c == ")" and stack[-1] == "(":
                    stack.pop()
                    continue
                if c == "]" and stack[-1] == "[":
                    stack.pop()
                    continue
                if c == "}" and stack[-1] == "{":
                    stack.pop()
                    continue
            stack.append(c)

        return len(stack) == 0