from functools import cache

class Solution:
    def integerBreak(self, n: int) -> int:  
        dp = {1: 1}

        for i in range(2, n + 1):
            dp[i] = 0 if i == n else i
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] * dp[i - j])
        return dp[n]
        """
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
        """