class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 1, 2, 8] [48, 24, 12, 8]
        res = []
        #left:
        prefix = 1
        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
        return res