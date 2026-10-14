class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = [] # (i, t)
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                tmp = stack.pop()
                res[tmp[0]] = i - tmp[0]
            
            stack.append((i, t))

        return res