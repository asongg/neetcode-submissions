class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for num in nums:
            heapq.heappush(res, num)
            while len(res) > k:
                heapq.heappop(res)
        kth = heapq.heappop(res)
        return kth