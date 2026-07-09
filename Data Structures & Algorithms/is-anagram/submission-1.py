class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(t) != len(s)):
            return False
        for char in s:
            if char in t:
                t = t.replace(char, '', 1)
        if(len(t) == 0):
            return True
        else:
            return False