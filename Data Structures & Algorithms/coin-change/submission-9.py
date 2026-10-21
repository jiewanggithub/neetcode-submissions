from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def dfs(amount_):
            if amount_ == 0:
                return 0
            
            if amount_ < 0:
                return float('INF')
            
            res = float('INF')
            for coin in coins:
                res = min(res, dfs(amount_ - coin) + 1)
            return res
        
        ans = dfs(amount)
        return ans if ans != float('INF') else -1