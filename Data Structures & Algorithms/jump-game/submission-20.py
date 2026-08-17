class Solution:
    def canJump(self, nums: List[int]) -> bool:
        best = nums[0]
        for i in range(1,len(nums)):
            if i <= best:
                best = max(best, nums[i] + i)
        return best >= len(nums) - 1