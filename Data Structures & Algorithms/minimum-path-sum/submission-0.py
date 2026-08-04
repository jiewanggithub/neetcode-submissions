from functools import cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        
        @cache
        def dfs(x, y):
            if x >= ROW or y >= COL:
                return float('inf')
            
            if x == ROW - 1 and y == COL - 1:
                return grid[x][y]
                
            return grid[x][y] + min(dfs(x+1, y), dfs(x, y+1))
            
        return dfs(0, 0)
