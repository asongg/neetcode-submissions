class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, path, sum):
            if sum > target or i == len(nums):
                return
            elif sum == target:
                res.append(path.copy())
                return
            for idx in range(i, len(nums)):
                path.append(nums[idx])
                sum += nums[idx]
                backtrack(idx, path,sum)
                path.pop()
                sum -= nums[idx]
        backtrack(0, [], 0)
        return res