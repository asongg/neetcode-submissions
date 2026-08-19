"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        res = [intervals[0]]
        for intv in intervals[1:]:
            start, end = intv.start, intv.end
            prev_end = res[-1].end
            if start < prev_end:
                return False
            else:
                res.append(intv)
        return True