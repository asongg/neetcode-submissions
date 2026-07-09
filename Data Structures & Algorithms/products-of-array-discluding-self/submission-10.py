class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zerod_total = 1
        num_zeros = 0
        for i in nums:
            total *= i
            if i != 0:
                zerod_total *= i
            else:
                num_zeros += 1
        
        out = []
        for j in nums:
            if j != 0:
                out.append(total//j)
            else:
                if num_zeros == 1:
                    out.append(zerod_total)
                elif num_zeros > 1:
                    out.append(0)
        
        return out