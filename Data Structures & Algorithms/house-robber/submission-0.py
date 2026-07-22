class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = dict()
        def dfs(i):
            if i < 0:
                return 0
            if i == 0: 
                return nums[i]
            if i in memo: return memo[i]
            memo[i] = max(dfs(i-1), dfs(i-2)+nums[i])
            return memo[i]
        return dfs(len(nums)-1)