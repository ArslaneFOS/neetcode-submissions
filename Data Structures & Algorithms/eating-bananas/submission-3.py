class Solution:
    def getTotalHours(self, piles: List[int], k: int):
        total = 0
        for pile in piles:
            total += math.ceil(pile/k)
        return total


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #rates = [i for i in range(1, topk+1)]

        low, high = 1, max(piles)
        res = low
        while low<=high:
            k = (low + high) // 2

            total = self.getTotalHours(piles, k)

            if total <= h:
                res = k
                high = k - 1

            else:
                low = k + 1

        return res
