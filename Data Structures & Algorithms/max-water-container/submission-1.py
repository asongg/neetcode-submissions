class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Two pointer approach, but what exactly do you keep track of that allows you
        # to determine whether to go left or right after an index?
        # area = min(heights[l],heights[r]) * (l-r)
        l = 0
        r = len(heights) - 1
        out = -1
        while l < r:
            if heights[l] < heights[r]:
                out = max(out, (heights[l]*(r-l)))
                l += 1
            elif heights[r] <= heights[l]:
                out = max(out, (heights[r]*(r-l)))
                r -= 1
        return out