class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        x1, y1 = 0, 0
        for x2, y2 in points:
            dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
            heapq.heappush(res, (-dist, [x2, y2]))
            while len(res) > k:
                heapq.heappop(res)
        closest = []
        for point in res:
            closest.append(point[1])
        return closest