class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        islands = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row,col)
                    islands += 1
        return islands