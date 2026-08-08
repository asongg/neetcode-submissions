class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        res = ""
        lenres = 0

        for left in range(n - 1, -1, -1):
            for right in range(left, n):
                if s[left] == s[right] and (
                    right - left <= 2 or dp[left + 1][right - 1]
                ):
                    dp[left][right] = True

                    if right - left + 1 > lenres:
                        lenres = right - left + 1
                        res = s[left:right + 1]

        return res