class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        h = len(grid)
        l = len(grid[0])

        def dfs(y: int, x: int):
            if (y >= h or x >= l) or grid[y][x] == '0':
                return

            grid[y][x] = '0'
            if y + 1 < h: dfs(y + 1, x)
            if x + 1 < l: dfs(y, x + 1)
            if y - 1 >= 0: dfs(y - 1, x)
            if x - 1 >= 0: dfs(y, x - 1)
            return

        for i in range(h):
            for j in range(l):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islands += 1

        return islands
        