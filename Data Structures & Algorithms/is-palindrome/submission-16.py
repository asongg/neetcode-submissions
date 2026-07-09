class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for i in range(len(s)):
            if s[i].isalnum(): new += s[i]
        l = 0
        r = len(new) - 1
        while l < r:
            if new[l].lower() != new[r].lower(): 
                return False
            l += 1
            r -= 1
        return True