class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper = max(piles)
        l = 1
        result = upper
        while l <= upper:
            mid = (upper + l) // 2
            candidate = 0
            for i in range(len(piles)):
                candidate += (piles[i] + mid - 1) // mid
            if candidate > h:
                l = mid + 1
            elif candidate <= h:
                result = mid
                upper = mid - 1
        return l