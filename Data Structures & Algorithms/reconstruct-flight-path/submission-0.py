class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, des in tickets:
            heapq.heappush(graph[src], des)
        
        res = []
        def dfs(src):
            while graph[src]:
                nei = heapq.heappop(graph[src])
                dfs(nei)
            res.append(src)
        dfs("JFK")
        return res[::-1]
