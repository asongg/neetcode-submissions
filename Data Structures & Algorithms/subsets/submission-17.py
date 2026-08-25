class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, path):
            res.append(path.copy())
            for idx in range(i, len(nums)):
                path.append(nums[idx])
                backtrack(idx+1, path)
                path.pop()
        backtrack(0, [])
        return res