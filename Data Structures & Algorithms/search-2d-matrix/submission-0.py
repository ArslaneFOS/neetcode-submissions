class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_ranges = [(row[0], row[-1]) for row in matrix]

        low, high = 0, len(row_ranges) - 1
        probable_row = []
        while low <= high:
            m = low + (high - low)//2

            if target < row_ranges[m][0]:
                high = m - 1
            elif target > row_ranges[m][1]:
                low = m + 1
            else:
                probable_row = matrix[m]
                break

        if not probable_row:
            return False

        low, high = 0, len(probable_row) - 1
        while low <= high:
            m = low + (high - low)//2

            if probable_row[m] < target:
                low = m + 1
            elif probable_row[m] > target:
                high = m - 1
            else:
                return True
        return False