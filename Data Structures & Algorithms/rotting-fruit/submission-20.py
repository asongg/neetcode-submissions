class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        start = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    start.append((r,c))
        q = deque(start)
        time = 0
        while q:
            tempLen = len(q)
            for i in range(tempLen):
                row, col = q.popleft()
                if row + 1 < ROWS and grid[row+1][col] == 1:
                    grid[row+1][col] = 2
                    q.append((row+1, col))
                if col + 1 < COLS and grid[row][col+1] == 1:
                    grid[row][col+1] = 2
                    q.append((row, col+1))
                if row - 1 >= 0 and grid[row-1][col] == 1:
                    grid[row-1][col] = 2
                    q.append((row-1, col))
                if col - 1 >= 0 and grid[row][col-1] == 1:
                    grid[row][col-1] = 2
                    q.append((row, col-1))
            time += 1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return max(0, time-1)