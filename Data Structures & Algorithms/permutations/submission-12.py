class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            if len(path) > len(nums):
                return
            for i in range(len(nums)):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    backtrack(path)
                    used[i] = False
                    path.pop()
        backtrack([])
        return res