class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []


        def dfs(i):
            if len(path) == k:
                res.append(path.copy())
                return 
            if i > n:
                return 
            
            dfs(i+1)
            path.append(i)
            dfs(i+1)
            path.pop()
        
        dfs(1)
        return res