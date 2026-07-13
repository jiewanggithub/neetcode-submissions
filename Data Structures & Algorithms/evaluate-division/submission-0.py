class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 1. creating graph 
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])
        
        def bfs(start, target):
            if start not in adj or target not in adj:
                return -1 
            
            q, visited = deque(), set()
            q.append([start, 1])
            visited.add(start)

            while q:
                n, w = q.popleft()
                if n == target:
                    return w 
                
                for nei, weight in adj[n]:
                    if nei not in visited:
                        q.append([nei, w * weight])
                        visited.add(nei)
            return -1

        return [bfs(s, t) for s, t in queries]