class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        results_stack : List[int] = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token in operators:
                # evaluate
                val2 = results_stack.pop()
                val1 = results_stack.pop()
                if token == "+": result = val1 + val2
                elif token == "-": result = val1 - val2
                elif token == "*": result = val1 * val2
                else: result = int(val1 / val2)
                results_stack.append(result)
            else:
                results_stack.append(int(token))

        return results_stack[-1]