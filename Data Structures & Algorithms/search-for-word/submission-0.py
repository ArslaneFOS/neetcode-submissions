class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(i, r, c) -> bool:
            if i == len(word):
                return True

            if (r < 0 
                or r >= ROWS 
                or c < 0 
                or c >= COLS 
                or board[r][c] != word[i]):

                return False

            temp = board[r][c]
            board[r][c] = '#'

            found = (
                dfs(i + 1, r - 1, c) or
                dfs(i + 1, r + 1, c) or
                dfs(i + 1, r, c - 1) or
                dfs(i + 1, r, c + 1)
            )

            board[r][c] = temp

            return found

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c):
                    return True

        return False