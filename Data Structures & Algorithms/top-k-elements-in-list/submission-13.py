class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for i in nums:
            if i not in freq: freq[i] = 0
            freq[i] += 1
        
        q = [0] * k 
        heapq.heapify(q)
        for v in freq.values():
            if v > q[0]:
                heapq.heappop(q)
                heapq.heappush(q, v)
        
        out = []
        for k, v in freq.items():
            if v in q:
                out.append(k)
        return out
        