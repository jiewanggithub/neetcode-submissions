from functools import cache 
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * (COL + 1) for _ in range(ROW + 1)]
        if obstacleGrid[ROW-1][COL-1] == 0:
            dp[ROW-1][COL-1] = 1

        for i in range(ROW - 1, -1, -1):
            for j in range(COL - 1, -1, -1):   
                if obstacleGrid[i][j] == 1:
                    continue 
                else:
                    dp[i][j] += dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]