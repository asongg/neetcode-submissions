class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        stack.append((temperatures[0], 0))
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[len(stack)-1][0]:
                res[stack[len(stack)-1][1]] = i - stack[len(stack)-1][1]
                stack.pop(len(stack)-1)
            stack.append((temperatures[i], i))
        return res