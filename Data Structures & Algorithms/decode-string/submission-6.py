class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                add = ""
                while stack and stack[-1] != '[':
                    add = stack.pop() + add
                stack.pop()  # -> '['
                multiplier = ""
                while stack and stack[-1] in digits:
                    multiplier = stack.pop() + multiplier
                multiplier = int(multiplier)
                add = multiplier * add
                stack.append(add)

        return "".join(stack)