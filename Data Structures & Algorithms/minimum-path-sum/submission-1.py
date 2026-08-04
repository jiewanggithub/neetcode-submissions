from functools import cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        
        dp = [[float("inf")] * (COL + 1) for _ in range(ROW + 1)]

        for i in range(ROW - 1, -1, -1):
            for j in range(COL - 1, -1, -1):
                if i == ROW - 1 and j == COL - 1:
                    dp[i][j] = grid[i][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
        return dp[0][0]