from functools import cache
import math

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(1, math.isqrt(i) + 1):
                square = j * j
                dp[i] = min(dp[i], 1 + dp[i - square])
        return dp[n]
