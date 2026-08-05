class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(q):
            seen = set()
            while q:
                curr = q.popleft()
                r, c = curr[0], curr[1]
                if curr in seen:
                    continue
                seen.add(curr)
                if r+1 < ROWS and heights[r][c] <= heights[r+1][c]:
                    q.append(tuple([r+1,c]))
                if r-1 >= 0 and heights[r][c] <= heights[r-1][c]:
                    q.append(tuple([r-1,c]))
                if c+1 < COLS and heights[r][c] <= heights[r][c+1]:
                    q.append(tuple([r,c+1]))
                if c-1 >= 0 and heights[r][c] <= heights[r][c-1]:
                    q.append(tuple([r,c-1]))
            return seen
        
        start = []
        ROWS, COLS = len(heights), len(heights[0])
        for r in range(ROWS):
            start.append((r,0))
        for c in range(COLS):
            start.append((0,c))
        queue = deque(start)
        atlantic = bfs(queue)
        start = []
        for r in range(ROWS):
            start.append((r, COLS-1))
        for c in range(COLS):
            start.append((ROWS-1,c))
        queue = deque(start)
        pacific = bfs(queue)
        return [list(cell) for cell in pacific & atlantic]
        