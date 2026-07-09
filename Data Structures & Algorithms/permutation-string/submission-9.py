class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s.replace('a', 'A', 2)
        freq1 = [0] * 26
        freq2 = [0] * 26
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1
        l = 0
        r = len(s1) - 1
        while r < len(s2) - 1:
            if freq1 == freq2:
                return True
            else:
                freq2[ord(s2[l]) - ord('a')] -= 1
                l += 1
                r += 1
                freq2[ord(s2[r]) - ord('a')] += 1
        return freq1 == freq2