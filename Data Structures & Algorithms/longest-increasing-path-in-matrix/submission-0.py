from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        @cache 
        def dfs(a, b):
            res = 1
            for x, y in direction:
                dx, dy = a + x, b + y
                if (not(dx < 0 or dy < 0 or dx >= ROWS or dy >= COLS) and 
                matrix[a][b] < matrix[dx][dy]):
                    res = max(res, 1 + dfs(dx, dy))

            return res

        return max(dfs(x, y) for x in range(ROWS) for y in range(COLS))
            
            
            