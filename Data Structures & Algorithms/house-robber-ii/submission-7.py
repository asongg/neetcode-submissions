class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_lin(houses):
            memo = dict()
            def dfs(i):
                if i < 0:
                    return 0
                if i == 0: 
                    return houses[i]
                if i in memo: return memo[i]
                memo[i] = max(dfs(i-1), dfs(i-2)+houses[i])
                return memo[i]
            return dfs(len(houses)-1)
        return max(rob_lin(nums[:len(nums)-1]), rob_lin(nums[1:]))