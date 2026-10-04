class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        res = []
        for i in range(len(intervals)):
            if end < intervals[i][0]:
                res.append([start, end])
                res += intervals[i:]
                return res 
            elif start > intervals[i][1]:
                res.append(intervals[i]) 
            else:
                start, end = (min(start, intervals[i][0]), max(end, intervals[i][1]))
        res.append([start, end])
        return res 
