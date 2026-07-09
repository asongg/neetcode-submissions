class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs[1:]:
            temp = ""
            for i in range(len(prefix)):
                if i >= len(word) or word[i] != prefix[i]:
                    break
                temp += prefix[i]
            prefix = temp
        return prefix