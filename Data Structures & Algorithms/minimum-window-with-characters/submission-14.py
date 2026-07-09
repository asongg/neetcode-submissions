class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        freq2 = dict()
        for i in range(len(t)):
            freq2[t[i]] = 1 + freq2.get(t[i], 0)
        l = 0
        freq1 = dict()
        have, need = 0, len(freq2)
        res, resLen = [-1, -1], float("infinity")
        for j in range(len(s)):
            freq1[s[j]] = 1 + freq1.get(s[j], 0)
            if s[j] in freq2 and freq1[s[j]] == freq2[s[j]]:
                have += 1
            while have == need:
                if (j - l + 1) < resLen:
                    resLen = j - l + 1
                    res = [l, j]
                freq1[s[l]] -= 1
                if s[l] in freq2 and freq1[s[l]] < freq2[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        if resLen == float("infinity"):
            return ""
        else:
            print(r)
            return s[l : r+1]