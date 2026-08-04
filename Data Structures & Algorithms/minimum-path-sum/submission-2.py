from functools import cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        
        dp = [float("inf")] * (COL + 1)
        dp[COL - 1] = 0

        for i in range(ROW - 1, -1, -1):
            for j in range(COL - 1, -1, -1):
                    dp[j] = grid[i][j] + min(dp[j], dp[j+1])
        return dp[0]