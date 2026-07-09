class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxLeft = height[0]
        maxRight = height[len(height)-1]
        total = 0
        while l <= r:
            if maxLeft <= maxRight:
                if maxLeft - height[l] > 0: total += maxLeft - height[l]
                maxLeft = max(maxLeft, height[l])
                l += 1
            else:
                if maxRight - height[r] > 0: total += maxRight - height[r]
                maxRight = max(maxRight, height[r])
                r -= 1
        return total
