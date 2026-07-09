class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        for k,v in d.items():
            if v > len(nums)/2: return k
        