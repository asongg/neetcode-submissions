class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 1
        r = piles[-1]
        while l < r:
            time = 0
            mid = (l + r) // 2
            for i in piles:
                time += math.ceil(i / mid)
            if time <= h:
                r = mid
            else:
                l = mid + 1
        return l