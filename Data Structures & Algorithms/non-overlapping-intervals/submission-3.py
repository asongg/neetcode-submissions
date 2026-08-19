class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        overlap = 0
        res = [intervals[0]]
        for start, end in intervals[1:]:
            prev_end = res[-1][1]
            if start < prev_end:
                overlap += 1
                res[-1][1] = min(end, prev_end)
            else:
                res.append([start, end])
        return overlap
