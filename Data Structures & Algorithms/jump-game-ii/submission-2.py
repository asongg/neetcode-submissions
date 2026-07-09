class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l,r = 0,0
        while r < len(nums) - 1:
            end = r
            for i in range(l, r+1):
                end = max(end, i+nums[i])
            l = r + 1
            r = end
            jumps += 1
        return jumps