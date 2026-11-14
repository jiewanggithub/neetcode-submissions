class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)

        for i, man in enumerate(manager):
            if man != -1:
                adj[man].append(i)
        
        res = 0
        q = deque([(0, headID)])
        
        while q:
            time, idx = q.popleft()
            res = max(res, time)

            for nei in adj[idx]:
                q.append([time + informTime[idx], nei])
        return res 

            

