class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers approach
        # lower height bar moves towards higher
        # eval the area at each combo, always store the max
        # tie, just choose random one
        l = 0
        r = len(heights) - 1
        res = -1
        while r > l:
            res = max(res, (r-l)*min(heights[r],heights[l]))
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return res