class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()

        for i in strs:
            curr = str(sorted(i))
            if curr in d.keys():
                d[curr].append(i)
            else:
                d[curr] = [i]
        
        out = []
        for key in d:
            out.append(d[key])
        
        return out