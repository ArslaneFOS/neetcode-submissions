class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        results_stack : List[int] = []
        operators = {"+", "-", "*", "/"}

        for i in range(len(tokens)):
            if tokens[i] in operators:
                # evaluate
                val2 = results_stack.pop()
                val1 = results_stack.pop()
                operator = tokens[i]
                result : int
                if operator == "+":
                    result = val1 + val2
                elif operator == "-":
                    result = val1 - val2
                elif operator == "*":
                    result = val1 * val2
                else:
                    result = int(val1 / val2)
                results_stack.append(result)

            else:
                results_stack.append(int(tokens[i]))

        return results_stack[-1]