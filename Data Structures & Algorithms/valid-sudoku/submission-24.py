class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        d = dict()
        for r in range(ROWS):
            seen = set()
            for c in range(COLS):
                if board[r][c] in seen:
                    return False
                if board[r][c] != '.':
                    seen.add(board[r][c])
                if (r//3, c//3) not in d:
                    d[(r//3,c//3)] = set()
        for c in range(COLS):
            seen = set()
            for r in range(ROWS):
                if board[r][c] in seen:
                    return False
                if board[r][c] != '.':
                    seen.add(board[r][c])
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in d[(r//3,c//3)]:
                    return False
                if board[r][c] != '.':
                    d[(r//3,c//3)].add(board[r][c])
        return True