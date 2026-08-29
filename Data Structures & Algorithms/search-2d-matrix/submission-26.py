class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l = 0
        r = ROWS - 1
        while l < r:
            mid = (l + r) // 2
            if target < matrix[mid][0]:
                r = mid
            elif target > matrix[mid][COLS-1]:
                l = mid + 1
            else:
                l = mid
                break
        row = l
        l = 0
        r = COLS - 1
        while l < r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid
            else: return True
        return matrix[row][l] == target