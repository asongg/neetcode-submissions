class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(set)
        row, col = len(board), len(board[0])
        for r in range(row):
            for c in range(col):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        
        return True