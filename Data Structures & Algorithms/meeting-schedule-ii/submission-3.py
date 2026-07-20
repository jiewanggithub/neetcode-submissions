"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        schedule = defaultdict(int)

        for i in range(len(intervals)):
            srt, end = intervals[i].start, intervals[i].end
            for j in range(srt, end):
                schedule[j] += 1
        
        return max(schedule.values())