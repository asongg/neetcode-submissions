class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        winMax = []
        for i in range(k):
            window.append([nums[i] * -1, i])
        heapq.heapify(window)
        winMax.append(window[0][0] * -1)
        l = 0
        while k < len(nums):
            heapq.heappush(window, [nums[k] * -1, k])
            while window[0][1] <= l or window[0][1] > k:
                heapq.heappop(window)
            winMax.append(window[0][0] * -1)
            l += 1
            k += 1
        return winMax
            