class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        srt, end = intervals[0]
        for i in range(1, len(intervals)):
            srt2, end2 = intervals[i]

            if end < srt2:
                res.append([srt, end])
                srt, end = srt2, end2 
            else: 
                srt = min(srt, srt2)
                end = max(end, end2)
        res.append([srt, end])
        return res

        """
            [1, 2] [1, 3]
            srt, end: [1, 2]


        """