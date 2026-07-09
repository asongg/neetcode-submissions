class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def bfs(row, col):
            if row >= ROWS or col >= COLS or min(row,col) < 0 or grid[row][col] == 0:
                return
            grid[row][col] = 0
            self.count += 1
            bfs(row+1, col)
            bfs(row, col+1)
            bfs(row-1, col)
            bfs(row, col-1)
        ret = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    self.count = 0
                    bfs(r,c)
                    ret = max(ret,self.count)
        return ret
