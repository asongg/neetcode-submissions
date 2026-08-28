class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def cell(r, c):
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == -1: return
            q.append([r,c])
            visit.add((r,c))
        q = deque()
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append([row,col])
                    visit.add((row,col))
        dist = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                cell(row+1, col)
                cell(row,col+1)
                cell(row-1,col)
                cell(row,col-1)
            dist += 1
