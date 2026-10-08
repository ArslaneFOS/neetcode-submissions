class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS = len(grid)
        COLS = len(grid[0])

        def sinkIsland(r, c):
            # q = collections.deque([(r, c)])

            # while q:
            #     cr, cc = q.popleft()
            #     grid[cr][cc] = "0"

            #     for dr, dc in DIRS:
            #         nr, nc = cr + dr, cc + dc

            #         if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == "0":
            #             continue

            #         q.append((nr, nc))
            grid[r][c] = '0'
            
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == "0":
                    continue
                sinkIsland(nr, nc)

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count += 1
                    sinkIsland(r, c)

        return count