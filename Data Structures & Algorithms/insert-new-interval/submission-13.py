class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        before, after, during = [], [], []
        for start, end in intervals:
            if end < newInterval[0]:
                before.append([start,end])
            elif start > newInterval[1]:
                after.append([start,end])
            else:
                during.append([start,end])
        for start, end in before: res.append([start,end])
        if during: res.append([min(newInterval[0],during[0][0]), max(newInterval[1],during[-1][1])])
        else: res.append(newInterval)
        for start,end in after: res.append([start,end])
        return res