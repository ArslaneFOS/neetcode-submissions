class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque() # rotten fruits queue

        visited = set()

        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        minutes = 0

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc

                    if ROWS > nr >= 0 and COLS > nc >= 0 and (nr, nc) not in visited and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        visited.add((nr, nc))

            if q: minutes += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return minutes