class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(i, path):
            res.append(path.copy())
            for idx in range(i, len(nums)):
                if idx > i and nums[idx] == nums[idx-1]:
                    continue
                path.append(nums[idx])
                backtrack(idx+1, path)
                path.pop()
        backtrack(0, [])
        return res