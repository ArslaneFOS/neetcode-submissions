class Solution:    
    def bfs(self, root: int, adj: dict):
        h = 0
        q = deque([root])
        visited = set()

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                for n in adj[node]:
                    if n not in visited:
                        q.append(n)

                visited.add(node)
            if q: h += 1
        return h

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        heights = [] # (height, root)

        for i in range(n):
            heights.append((self.bfs(i, adj), i))

        heapq.heapify(heights)

        res = [heapq.heappop(heights)]

        while heights and heights[0][0] == res[0][0]:
            res.append(heapq.heappop(heights))

        return [r[1] for r in res]
