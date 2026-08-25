class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(i, path, sum):
            if sum == target:
                res.append(path.copy())
                return
            elif i == len(candidates):
                return
            
            for idx in range(i, len(candidates)):
                if idx > i and candidates[idx-1] == candidates[idx]:
                    continue
                elif sum + candidates[idx] > target: break
                path.append(candidates[idx])
                sum += candidates[idx]
                backtrack(idx+1, path, sum)
                path.pop()
                sum -= candidates[idx]
        backtrack(0, [], 0)
        return res    
                