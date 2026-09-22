class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        start, end = intervals[0][0], intervals[0][1]
        
        for s, e in intervals[1:]:
            if end > s:
                start = min(start, s)
                end = min(end, e)
                count += 1
            else:
                start, end = s, e
        
        return count