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
        minH = n

        for i in range(n):
            h = self.bfs(i, adj)
            heights.append((h, i))
            minH = min(minH, h)
            

        res = []

        for h, r in heights:
            if h == minH:
                res.append(r)


        return res
