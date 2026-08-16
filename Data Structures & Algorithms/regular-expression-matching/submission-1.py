from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        
        @cache 
        def dfs(i, j):
            if j == m:
                return i == n

            match = i < n and (s[i] == p[j] or p[j] == '.')

            if (j + 1) < m and p[j + 1] == "*":
                return (dfs(i, j + 2) or (match and dfs(i + 1, j))) 
            
            if match:
                return dfs(i + 1, j + 1)
            
            return False 

        return dfs(0, 0)

