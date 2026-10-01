class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}

        stack = []

        for token in tokens:
            if token in operators:
                val1 = stack.pop()
                val2 = stack.pop()
                res : int

                if token == "+":
                    res = val2 + val1
                elif token == "-":
                    res = val2 - val1
                elif token == "*":
                    res = val2 * val1
                else:
                    res = int(val2 / val1)

                stack.append(res)

            else:
                stack.append(int(token))
        
        return stack[-1]