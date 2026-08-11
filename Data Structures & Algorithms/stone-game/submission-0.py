from functools import cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        
        @cache 
        def dfs(i, j):
            if i == j:
                return piles[i]   

            take_left = piles[i] - dfs(i + 1, j)
            take_right = piles[j] - dfs(i, j - 1) 
            return max(take_left, take_right)

        return dfs(0, n - 1) > 0

            
            

