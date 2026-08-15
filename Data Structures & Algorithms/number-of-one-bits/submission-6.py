class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(31, -1, -1):
            temp = 2**i
            if n >= temp:
                n = n - temp
                res += 1
        return res