class Solution:
    def encode(self, strs: List[str]) -> str:
        self.idx = []
        out = ""
        for s in strs:
            self.idx.append(len(s))
            out += s
        return out
    def decode(self, s: str) -> List[str]:
        fin = []
        end = 0
        for i in self.idx:
            start, end = end, end + i
            fin.append(s[start:end])
        return fin