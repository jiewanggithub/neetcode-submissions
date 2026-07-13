class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for ui, vi, ti in times:
            adj[ui].append([ti, vi])
        
        pq = [(0, k)]
        visited = set()
        res = 0
        while pq:
            time, node = heapq.heappop(pq)
            
            if node in visited:
                continue 
            visited.add(node)
            res = time
            
            for weight, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(pq, (time + weight, nei))
        return res if n == len(visited) else -1
