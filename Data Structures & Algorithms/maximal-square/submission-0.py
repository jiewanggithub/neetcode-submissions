class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = {}
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i >= n or j >= m:
                return 0
            
            if matrix[i][j] == '0':
                return 0
            
            dp[(i, j)] = min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1)) + 1
            return dp[(i, j)]
        
        res = 0
        for i in range(n):
            for j in range(m):
                res = max(res, dfs(i, j))
        return res ** 2