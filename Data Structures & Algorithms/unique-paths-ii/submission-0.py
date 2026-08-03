from functools import cache 
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])

        @cache 
        def dfs(x, y):
            if x > ROW - 1 or y > COL - 1 or obstacleGrid[x][y] == 1:
                return 0

            if x == ROW - 1 and y == COL - 1:
                return 1

            return dfs(x + 1, y) + dfs(x, y + 1)

        return dfs(0, 0) 
        