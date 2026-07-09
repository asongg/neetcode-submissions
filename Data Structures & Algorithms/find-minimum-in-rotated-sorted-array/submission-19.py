class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        ans = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                ans = min(nums[l], ans)
                break
            mid = (r + l) // 2
            ans = min(nums[mid], ans)
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
            
        return ans
