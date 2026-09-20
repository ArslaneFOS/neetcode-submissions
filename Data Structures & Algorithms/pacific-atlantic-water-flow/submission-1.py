class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS = len(heights)
        COLS = len(heights[0])
        dirs = [(-1, 0),(1, 0),(0, -1),(0, 1)]

        def bfs(r, c) -> bool:
            if (r == 0 and c == COLS - 1) or (r == ROWS - 1 and c == 0):
                return True

            reachedA = False
            reachedP = False

            q = deque([(r, c)])
            visited = set()
            visited.add((r, c))

            while q:
                row, col = q.popleft()


                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc


                    if (0 <= nr < ROWS 
                        and 0 <= nc < COLS 
                        and heights[nr][nc] <= heights[row][col] 
                        and (nr, nc) not in visited):

                        if nr == 0 or nc == 0:
                            reachedP = True

                        if nr == ROWS - 1 or nc == COLS - 1:
                            reachedA = True

                        if reachedA and reachedP:
                            return True

                        q.append((nr, nc))
                        visited.add((nr, nc))

            return False


        for r in range(ROWS):
            for c in range(COLS):
                if bfs(r, c): res.append([r, c])

        return res