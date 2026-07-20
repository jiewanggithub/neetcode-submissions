"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)

        if len(intervals) <= 1:
            return True
        
        srt, end = intervals[0].start, intervals[0].end
        for i in range(1, len(intervals)):
            if end > intervals[i].start:
                return False 
            srt, end = intervals[i].start, intervals[i].end
        return True 