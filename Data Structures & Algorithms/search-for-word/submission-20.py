class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        def backtrack(row, col, k):
            if k == len(word):
                return True
            if (min(row, col) < 0 or row >= len(board) or col >= len(board[0]) or word[k] != board[row][col] or (row, col) in path):
                return False
            path.add((row,col))
            res = ((backtrack(row+1, col, k+1)) or
            (backtrack(row, col+1, k+1)) or 
            (backtrack(row-1, col, k+1)) or
            (backtrack(row, col-1, k+1)))
            path.remove((row,col))
            return res
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False
