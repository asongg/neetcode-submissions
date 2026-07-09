class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1, list2 = [0]*26, [0]*26
        if len(s) != len(t): return False
        for i in range(len(s)):
            list1[ord('a')-ord(s[i])] += 1
            list2[ord('a')-ord(t[i])] += 1
        return (list1 == list2)