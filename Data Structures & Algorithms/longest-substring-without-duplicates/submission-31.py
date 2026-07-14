class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        res = 0
        seen = set()
        if len(s) != 0:
            seen.add(s[l])
        else:
            return 0
        while r < len(s):
            if s[r] in seen:
                res = max((r-l), res)
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])
            r += 1
        return max(res,(r-l))