class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        curr = nums[0]
        best = nums[0]
        res = 1
        for i in range(1,len(nums)):
            print(best)
            if curr >= len(nums) - 1:
                return res
            best = max(best, nums[i] + i)
            if i == curr:
                curr = best
                res += 1
            


                
        return res