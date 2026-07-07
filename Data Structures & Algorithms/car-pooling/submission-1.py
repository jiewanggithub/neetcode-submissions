class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        
        minHeap = []
        cur = 0     # num of passengers in the car 

        for numPas, start, end in trips:
            while minHeap and minHeap[0][0] <= start:
                prevEnd, prevNum = heapq.heappop(minHeap)
                cur -= prevNum 

            cur += numPas
            if cur > capacity:
                return False
            heapq.heappush(minHeap, [end, numPas])
        return True
