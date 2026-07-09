class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        best_len = 1
        temp = 1
        nums = sorted(nums)
        print(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] - 1:
                temp += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                temp = 1
            if temp > best_len:
                best_len = temp
        return best_len