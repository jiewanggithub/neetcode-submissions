from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dfs(s):
            if s == 0:
                return 0
            
            if s < 0:
                return float("inf")

            min_res = float("inf")
            for coin in coins:
                min_res = min(dfs(s - coin) + 1, min_res)
            
            return min_res
        
        ans = dfs(amount)
        return -1 if ans == float("inf") else ans