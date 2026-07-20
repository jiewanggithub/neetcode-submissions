from functools import cache

class Solution:
    def integerBreak(self, n: int) -> int:        
        @cache
        def dfs(n):
            if n == 1:
                return 1

            res = 0
            
            for i in range(1, n):
                res = max(res, i * max(dfs(n - i), n - i))
            return res 

        return dfs(n)