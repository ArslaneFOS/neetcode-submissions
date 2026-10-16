class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        d = (0, 1)
        r, c = 0, 0
        rStart, rEnd = 0, len(matrix) - 1
        cStart, cEnd = 0, len(matrix[0]) - 1
        res.append(matrix[r][c])

        while len(res) < len(matrix) * len(matrix[0]):
            
            dr, dc = d
            nr, nc = r + dr, c + dc

            if nr > rEnd:
                nr = r
                nc -= 1
                cEnd -= 1
                d = (0, -1)
            elif nr < rStart:
                nr = r
                nc += 1
                cStart += 1
                d = (0, 1)
            elif nc > cEnd:
                nc = c
                nr += 1
                rStart += 1
                d = (1, 0)
            elif nc < cStart:
                nc = c
                nr -= 1
                rEnd -= 1
                d = (-1, 0)

            r, c = nr, nc
            res.append(matrix[r][c])
        return res