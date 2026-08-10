from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def dfs(i, s):
            if s == 0:
                return 1

            if i == len(coins):
                return 0

            if s < 0:
                return 0
            
            return dfs(i, s - coins[i]) + dfs(i + 1, s)

        return dfs(0, amount)
        
        