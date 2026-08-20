"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        ends = [intervals[0].end]
        heapq.heapify(ends)
        for intv in intervals[1:]:
            start, end = intv.start, intv.end
            if start >= ends[0]:
                heapq.heappop(ends)
            heapq.heappush(ends, end)
        return len(ends)