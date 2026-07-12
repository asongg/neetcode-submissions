class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 2: 1, 20: 1, 4: 1, 10: 1, 3: 3, 5: 4
        # check for your -1 neighbor, if it exists add its value to your chain.
        # check if your +1 neighbor exists. if it does, then while u have a +1 neighbor,
        # keep on 

        d = dict()
        for i in nums:
            if i in d:
                continue
            sum = 1
            tempLeft = i-1
            while tempLeft in d:
                sum += d[tempLeft]
                d[tempLeft] = 0
                tempLeft -= 1
            tempRight = i+1
            while tempRight in d:
                sum += d[tempRight]
                d[tempRight] = 0
                tempRight += 1
            d[i] = sum
        return max(d.values()) if d else 0