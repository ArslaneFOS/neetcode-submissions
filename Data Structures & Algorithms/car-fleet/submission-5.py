class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        stack = []

        for p, s in cars:
            time = (target - p) / s

            if not stack:
                stack.append((time, p, s))

            elif time > stack[-1][0]:
                stack.append((time, p, s))

        return len(stack)