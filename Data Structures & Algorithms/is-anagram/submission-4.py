class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        for i in range(len(s)):
            curr = s[i]
            if curr in d:
                d[curr] = d[curr] + 1
            else:
                d[curr] = 1
        
        for j in range(len(t)):
            curr = t[j]
            if curr in d:
                d[curr] = d[curr] - 1
            else:
                return False
        
        for k in d:
            if d[k] != 0:
                return False
        return True

        