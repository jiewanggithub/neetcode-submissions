class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for start, end, cost in times:
            adj[start].append((end, cost))
        
        pq = []
        heapq.heappush(pq, (0, k))
        visited = set()
        res = 0

        while pq:
            dis, node = heapq.heappop(pq)
            if node in visited:
                continue 
            res = dis
            visited.add(node)

            for des, cost in adj[node]:
                if des not in visited:
                    heapq.heappush(pq, (cost + res, des))
        return res if len(visited) == n else -1 
                