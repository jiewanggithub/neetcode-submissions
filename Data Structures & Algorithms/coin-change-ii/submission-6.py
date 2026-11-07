from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache 
        def dfs(total, i):
            if total > amount:
                return 0
            if total == amount:
                return 1
            
            cnt = 0
            for j in range(i, len(coins)):
                cnt += dfs(total + coins[j], j)
            return cnt
        return dfs(0, 0)