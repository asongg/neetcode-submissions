class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tempArr = []
        for i in range(len(nums)):
            if nums[i] in tempArr:
                return True
            tempArr.append(nums[i])
        return False