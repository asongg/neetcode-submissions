class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(path, sum, i):
            if sum > target or i > len(candidates):
                return
            elif sum == target:
                res.append(path[:])
                return
            for index in range(i, len(candidates)):
                if index > i and candidates[index] == candidates[index - 1]:
                    continue
                path.append(candidates[index])
                backtrack(path, sum + candidates[index], index+1)
                path.pop()
        backtrack([],0,0)
        return res