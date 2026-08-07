class Solution:
    def findMin(self, nums: List[int]) -> int:
        # min -> >right, > left
        l = 0
        r = len(nums)-1
        mid = (l+r)//2
        while l < r:
            if l == mid:
                return min(nums[l], nums[r])
            if nums[mid] > nums[r]:
                l = mid
            else:
                r = mid
            mid = (l + r) // 2
        return nums[r]
            