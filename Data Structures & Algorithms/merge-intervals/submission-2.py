class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        left_start, left_end = intervals[0]
        res = []
        for right, interval in enumerate(intervals[1:]):
            start, end = interval
            if start > left_end:
                res.append([left_start, left_end])
                left_start, left_end = start, end 
            else:
                left_start = min(left_start, start)
                left_end = max(left_end, end)
        res.append([left_start, left_end])
        return res 
            
