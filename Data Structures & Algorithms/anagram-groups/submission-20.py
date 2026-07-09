class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch)-ord('a')] += 1
            freq = tuple(freq)
            d[freq].append(word)
        return(list(d.values()))