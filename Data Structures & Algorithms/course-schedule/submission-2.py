class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for a, b in prerequisites:
            adj[b].append(a)
        
        visited = [0 for i in range(numCourses)]
        """
            visited[i] == 0: unvisited
            visited[i] == 1: visiting
            visited[i] == 2: visited
        """ 

        def dfs(i):
            if visited[i] == 2:
                return True
            if visited[i] == 1:
                return False
            
            visited[i] = 1
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            visited[i] = 2
            return True  
        
        for i in range(numCourses):
            if not dfs(i):
                return False 
        return True 
        
        