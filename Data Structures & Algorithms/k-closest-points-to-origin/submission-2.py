class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        distance_points = [((x)**2 + (y)**2, [x, y]) for x, y in points]
        heapq.heapify(distance_points)

        for i in range(k):
            res.append(heapq.heappop(distance_points)[1])
            
        return res