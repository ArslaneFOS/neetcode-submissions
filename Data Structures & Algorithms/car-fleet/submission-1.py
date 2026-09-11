class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse=True, key=lambda x : x[0])

        stack = []

        for p, s in cars:
            t = (target - p)/s
            if not stack:
                stack.append(t)
                continue
            elif stack and t > stack[-1]:
                stack.append(t)
                
        return len(stack)
            