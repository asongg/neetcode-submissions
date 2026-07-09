class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a, b = 0, 1
        sum = nums[a] + nums[b]
        while(sum != target):
            if b != len(nums)-1:
                b += 1
            else:
                a += 1
                b = a + 1
            sum = nums[a] + nums[b]
        return [a,b]