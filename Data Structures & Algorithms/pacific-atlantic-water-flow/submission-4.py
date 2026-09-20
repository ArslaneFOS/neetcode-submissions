class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # res = []
        ROWS = len(heights)
        COLS = len(heights[0])
        dirs = [(-1, 0),(1, 0),(0, -1),(0, 1)]

        atlantic = set()
        atlantic_q = deque()

        pacific = set()
        pacific_q = deque()

        def bfs(visited : set, queue : deque):
            while queue:
                row, col = queue.popleft()

                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc

                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        (nr, nc) not in visited and
                        heights[nr][nc] >= heights[row][col]
                    ):
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(ROWS):
            pacific_q.append((r, 0))
            pacific.add((r, 0))

            atlantic_q.append((r, COLS - 1))
            atlantic.add((r, COLS - 1))

        for c in range(COLS):
            pacific_q.append((0, c))
            pacific.add((0, c))

            atlantic_q.append((ROWS - 1, c))
            atlantic.add((ROWS - 1, c))

        bfs(pacific, pacific_q)
        bfs(atlantic, atlantic_q)
        
        return [[r, c] for r in range(ROWS) for c in range(COLS) if (r, c) in pacific and (r, c) in atlantic]