class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for i in nums:
            if i in freq: freq[i] += 1
            else:
                freq[i] = 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, value in freq.items():
            buckets[value].append(key)
        
        res = []
        for i in range(len(nums), 0, -1):
            for j in buckets[i]:
                if len(res) == k: 
                    return res
                res.append(j)
        return res
