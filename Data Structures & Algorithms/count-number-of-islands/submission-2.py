class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        dirs = [[1, 0],[-1, 0],[0, 1],[0, -1]]
        COLS = len(grid)
        ROWS = len(grid[0])

        def dfs(y: int, x: int):
            if x < 0 or y < 0 or y >= COLS or x >= ROWS or grid[y][x] == '0':
                return

            grid[y][x] = '0'
            for dy, dx in dirs:
                dfs(y + dy, x + dx)

        for i in range(COLS):
            for j in range(ROWS):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islands += 1

        return islands
        