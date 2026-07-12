class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4,-1,-1,0,1,2]
        nums.sort()
        res = list()
        for i in range(len(nums)):
            l = i+1
            r = len(nums) - 1
            while r > l:
                tempSum = nums[i] + nums[l] + nums[r]
                if tempSum > 0:
                    r -= 1
                    continue
                elif tempSum < 0:
                    l += 1
                    continue
                if [nums[i], nums[l], nums[r]] not in res:
                    res.append([nums[i], nums[l], nums[r]])
                r -= 1
                l += 1
        return res