class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0
        while q or maxHeap:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt += 1
                if cnt < 0: 
                    q.append((time + n, cnt))

            if q and q[0][0] == time:
                heapq.heappush(maxHeap, q.popleft()[1])

        return time