class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # creating a graph 
        graph = {i:[] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        res = []
        min_height = float("inf")
        
        for i in range(n):
            q = deque([i])
            visited = {i}       
            height = -1
            while q:
                level_size = len(q)
                height += 1
                
                for _ in range(level_size):
                    node = q.popleft()
                    for nei in graph[node]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            if height < min_height:
                min_height = height
                res = [i]
            elif height == min_height:
                res.append(i)
        return res
            