class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
        
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue 
                if not dfs(nei, node):
                    return False 

            return True
        
        if not dfs(0, -1):
            return False

        return len(visited) == n
                    

        
