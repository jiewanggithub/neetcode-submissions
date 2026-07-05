class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # maxheap 
        counter = Counter(tasks)
        maxHeap = [-cnt for cnt in counter.values()]    
        heapq.heapify(maxHeap)
        q = deque()

        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt += 1
                if cnt:
                    q.append([cnt, n + time])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time 
