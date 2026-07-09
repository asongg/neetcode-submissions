class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.replace(" ", "")
        t = t.replace(" ", "")
        if len(s) != len(t): return False
        s_count = dict()
        for i in range(0, len(s)):
            if s[i] not in s_count: s_count[s[i]] = 0
            s_count[s[i]] += 1

        t_count = dict()
        for j in range(0, len(t)):
            if t[j] not in t_count: t_count[t[j]] = 0
            t_count[t[j]] += 1
        
        for k, v in s_count.items():
            if k not in t_count or t_count[k] != v:
                return False
        return True
        