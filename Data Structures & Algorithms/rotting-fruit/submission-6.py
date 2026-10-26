class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        DIRS = [(-1,0), (1,0), (0,-1), (0,1)]
        ROWS = len(grid)
        COLS = len(grid[0])

        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1

            minutes += 1

        return minutes if fresh == 0 else -1
