class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            if len(path) > len(nums):
                return
            for i in range(len(nums)):
                if i not in used:
                    path.append(nums[i])
                    used.append(i)
                    backtrack(path,used)
                    used.pop()
                    path.pop()
        backtrack([],[])
        return res