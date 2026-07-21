class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        q = []
        for i, n in enumerate(queries):
            q.append((n, i))
        q.sort(key=lambda x:x[0])
        intervals.sort()

        interval_index = 0
        result = [-1] * len(queries)
        min_heap = []

        for n, i in q:
            while (interval_index < len(intervals) 
            and intervals[interval_index][0] <= n):
                left, right = intervals[interval_index]
                length = right - left + 1

                heapq.heappush(min_heap, (length, right))
                interval_index += 1
            
            while min_heap and min_heap[0][1] < n:
                heapq.heappop(min_heap)
            
            if min_heap:
                result[i] = min_heap[0][0]
        return result 
