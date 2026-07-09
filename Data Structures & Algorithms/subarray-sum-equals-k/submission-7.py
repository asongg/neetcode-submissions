class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        res = 0
        prefix = 0
        for x in nums:
            prefix += x
            res += count[prefix - k]
            count[prefix] += 1
        return res