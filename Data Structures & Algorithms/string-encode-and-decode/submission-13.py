class Solution:
    # ['hi', 'there', 'how', 'are']
    # hiHYGthereHYGhowHYGare
    # [2,5,3,3] -> created in encode by going through each element in strs and adding
    # len(strs[i]) to the list
    # hitherehoware -> created in encode
    # iterate through the list of lengths
    # hi
    # s = s[2:]

    def encode(self, strs: List[str]) -> str:
        self.lengths = []
        res = ""
        for s in strs:
            self.lengths.append(len(s))
            res += s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        for length in self.lengths:
            res.append(s[0:length])
            s = s[length:]
        return res