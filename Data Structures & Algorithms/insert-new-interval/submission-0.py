class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        srt, end = newInterval

        for left, right in intervals:
            if srt > right:
                res.append([left, right])
            
            elif end < left:
                res.append([srt, end])
                srt, end = left, right
            
            else:
                srt = min(left, srt)
                end = max(right, end)
        res.append([srt, end])
        return res