from functools import cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        @cache 
        def dfs(i, M):
            if i >= len(piles):
                return 0
            
            res = float("-inf")
            cnt = 0 
            for x in range(1, min(2 * M, len(piles) - i) + 1):
                cnt += piles[i + x - 1]
                res = max(res, cnt - dfs(i + x, max(M, x)))
            return res 
        
        diff = dfs(0, 1)

        return (sum(piles) + diff) // 2

