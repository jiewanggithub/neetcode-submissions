class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free_days = 0
        start_date, end_date = meetings[0]
        free_days += start_date - 1

        for start, end in meetings[1:]:
            if start > end_date:
                free_days += start - end_date - 1
            end_date = max(end_date, end)
        
        return free_days + days - end_date
