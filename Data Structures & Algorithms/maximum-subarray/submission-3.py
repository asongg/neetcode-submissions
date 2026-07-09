class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxSeen = float("-inf")
        for i in range(len(nums)):
            sum += nums[i]
            maxSeen = max(sum, maxSeen)
            if sum < 0:
                sum = 0
        return maxSeen