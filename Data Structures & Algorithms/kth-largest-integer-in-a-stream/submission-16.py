class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self.k = k
        for i in range(len(nums)):
            self.pq.append(nums[i])
        heapq.heapify(self.pq)
    def add(self, val: int) -> int:
        heapq.heappush(self.pq, (val))
        while len(self.pq) > self.k:
            heapq.heappop(self.pq)
        return self.pq[0]
