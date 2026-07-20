from functools import cache

class Solution:
    def integerBreak(self, n: int) -> int:        
        @cache
        def dfs(num):
            if num == 1:
                return 1

            res = 0 if n == num else num
            
            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                res = max(res, val)
            return res 

        return dfs(n)