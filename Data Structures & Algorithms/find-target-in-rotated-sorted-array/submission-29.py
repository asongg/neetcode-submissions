class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        mid = (l + r) // 2
        while l < r:
            if nums[mid] > nums[r]:
                if target >= nums[l] and target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if target <= nums[r] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid
            mid = (l + r)//2
        if nums[mid] == target:
            return mid
        else: return -1