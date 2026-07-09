class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for i in range(len(stones)):
            pq.append((stones[i] * -1))
        heapq.heapify(pq)
        while len(pq) > 0:
            if len(pq) == 1: return (heapq.heappop(pq) * -1) 
            stone1 = heapq.heappop(pq)
            stone2 = heapq.heappop(pq)
            diff = abs(stone1 - stone2)
            if diff != 0:
                heapq.heappush(pq, diff * -1)
        return (heapq.heappop(pq) * -1) if pq else 0