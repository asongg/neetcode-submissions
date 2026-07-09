class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dist = dict()
        for i in range(len(nums)):
            if nums[i] not in dist: dist[target-nums[i]] = i
            else: return [dist[nums[i]], i]