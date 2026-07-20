class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        srt, end = intervals[0]
        for i in range(1, len(intervals)):
            left, right = intervals[i]
            
            if left >= end:
                srt, end = left, right
            
            else:
                srt = min(srt, left)
                end = min(end, right)
                res += 1
        return res

        """
            [1, 3], [2, 4] [2, 5]
            [1, 4] [2, 5]

        """