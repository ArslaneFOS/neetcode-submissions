class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowsMap = defaultdict(set)
        colsMap = defaultdict(set)
        squaresMap = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == '.':
                    continue
                
                if (board[r][c] in rowsMap[r] or 
                board[r][c] in colsMap[c] or 
                board[r][c] in squaresMap[(r // 3, c // 3)]):
                    return False

                rowsMap[r].add(board[r][c])
                colsMap[c].add(board[r][c])
                squaresMap[(r // 3, c // 3)].add(board[r][c])
                

        return True