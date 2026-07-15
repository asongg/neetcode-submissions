class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for i in range(len(s)):
            if s[i] in d:
                if not stack: return False
                temp = stack.pop()
                if d[s[i]] != temp:
                    return False
            else:
                stack.append(s[i])
        if stack: return False
        else: return True