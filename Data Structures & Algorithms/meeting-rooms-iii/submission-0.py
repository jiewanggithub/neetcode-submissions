class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = {i: 0 for i in range(n)}

        busyHeap = []
        freeHeap = []

        for i in range(n):
            heapq.heappush(freeHeap, i)

        for i in range(len(meetings)):
            srt, end = meetings[i]
            while busyHeap and busyHeap[0][0] <= srt:
                ending, roomNum = heapq.heappop(busyHeap)
                heapq.heappush(freeHeap, roomNum)
            
            if freeHeap:
                roomNum = heapq.heappop(freeHeap)
                heapq.heappush(busyHeap, (end, roomNum))
                rooms[roomNum] += 1
            else:
                ending, roomNum = heapq.heappop(busyHeap)
                newEnding = ending + (end - srt)
                heapq.heappush(busyHeap, (newEnding,roomNum))
                rooms[roomNum] += 1
        
        max_ = 0
        room = 0
        for i in range(n):
            if rooms[i] > max_:
                room = i
                max_ = max(rooms[i], max_)
        return room

