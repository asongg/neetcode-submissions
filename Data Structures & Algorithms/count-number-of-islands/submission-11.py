class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            grid[r][c] = "0"
            if r+1 < len(grid) and grid[r+1][c] == "1":
                dfs(r+1,c)
            if c+1 < len(grid[0]) and grid[r][c+1] == "1":
                dfs(r,c+1)
            if r-1 >= 0 and grid[r-1][c] == "1":
                dfs(r-1,c)
            if c-1 >= 0 and grid[r][c-1] == "1":
                dfs(r,c-1)
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i,j)
        return res