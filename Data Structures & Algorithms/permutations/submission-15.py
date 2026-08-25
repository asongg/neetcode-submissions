class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, path, seen):
            if i == len(nums):
                res.append(path.copy())
                return
            i += 1
            for idx in range(len(nums)):
                if nums[idx] not in seen:
                    seen.add(nums[idx])
                    path.append(nums[idx])
                    backtrack(i, path, seen)
                    seen.remove(nums[idx])
                    path.pop()
                else:
                    continue
        backtrack(0, [], set())
        return res