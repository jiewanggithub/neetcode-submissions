class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        direction = {i:[] for i in range(n)}

        for a, b in edges:
            direction[a].append(b)
            direction[b].append(a)
        
        visited = set()

        def dfs(cur, parent):
            if cur in visited:
                return False
            
            visited.add(cur)
            for child in direction[cur]:
                if child == parent:
                    continue
                if not dfs(child, cur):
                    return False
            return True 
        
        if not dfs(0, -1):
            return False
        
        return len(visited) == n
