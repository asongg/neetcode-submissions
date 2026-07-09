class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac, atl = set(), set()
        ret = []
        def dfs(r, c,visit, prev):
            if (r,c) in visit or r >= ROWS or c >= COLS or min(r, c) < 0 or heights[r][c] < prev:
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
        for row in range(ROWS):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, COLS-1, atl, heights[row][COLS-1])
        for col in range(COLS):
            dfs(0, col, pac, heights[0][col])
            dfs(ROWS-1, col, atl, heights[ROWS-1][col])
        for row in range(ROWS):
            for col in range(COLS):
                if (row,col) in pac and (row,col) in atl:
                    ret.append((row,col))

        return ret
            