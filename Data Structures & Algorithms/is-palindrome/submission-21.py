class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while r > l:
            if not s[r].isalnum():
                r -= 1
                continue
            if not s[l].isalnum():
                l += 1
                continue
            if s[l].upper() != s[r].upper():
                return False
            r -= 1
            l += 1
        return True
