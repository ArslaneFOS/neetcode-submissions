class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}

        stack = []

        for token in tokens:
            if token in operators:
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                res : int

                if token == "+":
                    res = val2 + val1
                elif token == "-":
                    res = val2 - val1
                elif token == "*":
                    res = val2 * val1
                else:
                    res = int(val2 / val1)

                stack.append(str(res))

            else:
                stack.append(token)
        
        return int(stack[-1])