class Solution:
    def numDecodings(self, s: str) -> int:
        memo = defaultdict(int)
        def dp(i):
            if i > len(s)-1:
                return 1
            if i in memo: return memo[i]
            if s[i] != '0':
                memo[i] += dp(i+1)
            else:
                memo[i] = 0
            if i + 1 < len(s) and int(s[i:i+2]) >= 10 and int(s[i:i+2]) <= 26:
                memo[i] += dp(i+2)
            return memo[i]
        return dp(0)