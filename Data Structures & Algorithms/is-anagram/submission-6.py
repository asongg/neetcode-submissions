class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.replace(" ", "")
        t = t.replace(" ", "")
        s = sorted(s)
        t = sorted(t)
        i = 0
        if len(s) != len(t): return False
        while i < len(s):
            if s[i] != t[i]: return False
            i += 1
        return True

        