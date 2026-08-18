class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for j in range(n+1):
            num = 0
            n = j
            for i in range(31, -1, -1):
                temp = 2**i
                if n >= temp:
                    n = n - temp
                    num += 1
            res.append(num)
        return res