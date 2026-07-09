class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        if len(s) == 1: return 1
        if len(s) == 0: return 0
        l = 0
        best = 0
        seen.add(s[l])
        for r in range(1,len(s)):
            if s[r] in seen:
                
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])
            best = max(best, r - l + 1)
        return best