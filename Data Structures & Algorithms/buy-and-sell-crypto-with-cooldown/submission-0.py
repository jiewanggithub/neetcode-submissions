from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        @cache 
        def dfs(i, hasStock):
            if i >= len(prices):
                return 0
            
            if hasStock:
                return max(dfs(i + 2, 0) + prices[i], 
                dfs(i + 1, 1))
            return max(dfs(i + 1, 0), dfs(i + 1, 1) - prices[i])

        return dfs(0, 0)