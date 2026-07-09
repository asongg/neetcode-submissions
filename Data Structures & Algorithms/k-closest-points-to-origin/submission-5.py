
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for i in range(len(points)):
            x2 = points[i][0]
            y2 = points[i][1]
            euclid = (math.sqrt((0 - x2)**2 + (0 - y2)**2)) * -1
            heapq.heappush(dist, (euclid, points[i]))
            if len(dist) > k:
                heapq.heappop(dist)
        
        res = []
        while dist:
            res.append(heapq.heappop(dist)[1])
        return res