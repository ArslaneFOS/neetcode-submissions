class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack : List[tuple[int,int]] = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                it = stack.pop()
                result[it[0]] = i - it[0]

            stack.append((i, t))
        return result