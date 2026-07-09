class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for i in range(len(strs)):
            curr = strs[i].replace(" ", "")
            char_freq = [0] * 26
            for j in range(len(curr)):
                idx = ord(curr[j].lower()) - ord('a')
                char_freq[idx] += 1
            if tuple(char_freq) not in d: d[tuple(char_freq)] = []
            d[tuple(char_freq)].append(strs[i])
        return list(d.values())