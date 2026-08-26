class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(path, l, r):
            if l == n and r == n:
                res.append("".join(path.copy()))
                return
            if l < n:
                path.append("(")
                backtrack(path, l+1, r)
                path.pop()
            if r < l:
                path.append(")")
                backtrack(path, l, r+1)
                path.pop()
        backtrack([], 0, 0)
        return res