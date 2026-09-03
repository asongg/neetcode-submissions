class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i] * -1
        heapq.heapify(stones)
        while len(stones) > 1:
            elem1 = heapq.heappop(stones) * -1
            elem2 = heapq.heappop(stones) * -1
            print(stones)
            if elem1 == elem2: continue
            elif elem1 < elem2:
                heapq.heappush(stones, (elem2-elem1) * -1)
            elif elem2 < elem1:
                heapq.heappush(stones, (elem1-elem2) * -1)
        return stones[0] * -1 if stones else 0