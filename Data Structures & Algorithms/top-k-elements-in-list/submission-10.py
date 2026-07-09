class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()

        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1
        
        sorted_dict = dict(sorted(d.items(), key=lambda item: item[1],reverse=True))
        out = []
        count = 0
        for key in sorted_dict:
            out.append(key)
            count += 1
            if count == k:
                return out
        
        