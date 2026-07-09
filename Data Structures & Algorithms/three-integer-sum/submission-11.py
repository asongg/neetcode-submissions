class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # fix i, treat j and k as the two pointers
        # i = 0
        nums.sort()
        out = []
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp > 0:
                    k -= 1
                elif temp < 0:
                    j += 1
                else:
                    if [nums[i], nums[j], nums[k]] not in out:
                        out.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
        return out