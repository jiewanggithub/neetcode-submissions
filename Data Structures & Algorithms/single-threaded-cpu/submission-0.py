class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        n = len(tasks)

        for i, task in enumerate(tasks):
            tasks[i] = [task[0], task[1], i]

        tasks.sort()

        minHeap = []
        time = tasks[0][0]
        index = 0

        while len(res) < n:
            while index < n and tasks[index][0] <= time:
                enqueue, process, i = tasks[index]
                heapq.heappush(minHeap, [process, i])
                index += 1

            if minHeap:
                process, i = heapq.heappop(minHeap)
                res.append(i)
                time += process
            else:
                time = tasks[index][0]

        return res
            
        
            

