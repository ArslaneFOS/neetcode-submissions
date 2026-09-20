class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        INF = 2**31 - 1
        
        def bfs(q : deque):
            visited = set(q)

            steps = 1
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()

                    for dr, dc in dirs:
                        nr, nc = row + dr, col + dc

                        if ROWS > nr >= 0 and COLS > nc >= 0 and (nr, nc) not in visited and grid[nr][nc] not in [-1, 0]:
                            q.append((nr, nc))
                            visited.add((nr, nc))
                            grid[nr][nc] = steps
                steps += 1

        treasureQueue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    treasureQueue.append((r, c))

        
        bfs(treasureQueue)
        
