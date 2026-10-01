class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True) # O(n log(n))

        stack = []

        for p, s in cars: # O(n)
            time = (target - p) / s

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)

# -> O(n log(n))