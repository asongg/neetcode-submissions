class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            tempList = [0] * 26
            for i in word:
                tempList[(ord('a')-ord(i))] += 1
            d[tuple(tempList)].append(word)
        return list(d.values())