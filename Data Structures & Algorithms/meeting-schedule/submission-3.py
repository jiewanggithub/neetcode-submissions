"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True 
        intervals.sort(key=lambda x: x.start)
        start, end = intervals[0].start, intervals[0].end

        for itvl in intervals[1:]:
            if itvl.start < end:
                return False
            start, end = itvl.start, itvl.end
        return True