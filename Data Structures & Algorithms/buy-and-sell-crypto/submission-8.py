class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        res = 0
        while r + 1 < len(prices):
            if prices[l] > prices[r+1]:
                res = max(res, prices[r]-prices[l])
                l = r + 1
            elif prices[r] > prices[r+1]:
                res = max(res, prices[r]-prices[l])
            r += 1
        return max(res, prices[r]-prices[l])