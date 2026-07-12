class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        count = 0

        def dfs(cur):
            if cur in visited:
                return 
            
            visited.add(cur)
            for nei in graph[cur]:
                dfs(nei)
        
        for key, val in graph.items():
            if key not in visited:
                dfs(key)
                count += 1
        return count 