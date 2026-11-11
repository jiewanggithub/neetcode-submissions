from functools import cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @cache
        def dfs(i, M):
            if i == n:
                return 0

            if 2 * M >= n - i:
                return suffix[i]

            res = 0
            for X in range(1, min(n - i, 2*M) + 1):
                opponent = dfs(i + X, max(M, X))
                current = suffix[i] - opponent
                res = max(res, current)
        
            return res 

        return dfs(0, 1)
