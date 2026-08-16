class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        ROW, COL = len(board), len(board[0])
        seen = set()
        def backtrack(x, y, i):
            if x == ROW or y == COL or x < 0 or y < 0 or (x,y) in seen or word[i] != board[x][y]:
                return
            elif i == len(word)-1:
                nonlocal res
                res = True
                return
            else:
                i += 1
                seen.add((x,y))
                backtrack(x+1,y,i)
                backtrack(x-1,y,i)
                backtrack(x,y+1,i)
                backtrack(x,y-1,i)
                i -= 1
                seen.remove((x,y))
        for r in range(ROW):
            for c in range(COL):
                backtrack(r, c, 0)
        return res