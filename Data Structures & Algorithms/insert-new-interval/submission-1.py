class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insert_start, insert_end = newInterval
        res = []

        """
        [1, 2] [3, 5] [9, 10]          [6, 7]
        """
        for start, end in intervals:
            if insert_start > end:
                res.append([start, end])
            elif insert_end < start:
                res.append([insert_start, insert_end])
                insert_start, insert_end = start, end 
            else:
                insert_start = min(insert_start, start)
                insert_end = max(insert_end, end )
        res.append([insert_start, insert_end])            
        return res
                