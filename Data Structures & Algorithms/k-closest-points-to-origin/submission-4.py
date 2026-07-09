import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        x1 = 0
        y1 = 0
        for i in range(len(points)):
            x2 = points[i][0]
            y2 = points[i][1]
            euclid = (math.sqrt((x1 - x2)**2 + (y1 - y2)**2)) * -1
            heapq.heappush(dist, (euclid, points[i]))
            if len(dist) > k:
                heapq.heappop(dist)
        
        res = []
        while dist:
            res.append(heapq.heappop(dist)[1])
        return res