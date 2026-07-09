class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(path, sum, start):
            if sum > target:
                return
            elif sum == target:
                res.append(path[:])
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                sum += nums[i]
                backtrack(path[:], sum, i)
                path.pop()
                sum -= nums[i]
        backtrack([],0, 0)
        return res
                