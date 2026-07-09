class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for i in range(len(nums)):
            if len(pq) == k:
                if pq[0] < nums[i]:
                    heapq.heappop(pq)
                else: continue
            heapq.heappush(pq, nums[i])
        return pq[0]
            