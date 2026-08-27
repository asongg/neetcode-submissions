class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            grid[r][c] = 0
            temp = 1
            if r+1 < len(grid) and grid[r+1][c] == 1:
                temp += dfs(r+1,c)
            if c+1 < len(grid[0]) and grid[r][c+1] == 1:
                temp += dfs(r,c+1)
            if r-1 >= 0 and grid[r-1][c] == 1:
                temp += dfs(r-1,c)
            if c-1 >= 0 and grid[r][c-1] == 1:
                temp += dfs(r,c-1)
            return temp

        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    temp = dfs(row,col)
                    res = max(res, temp)
        return res