class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        row_has = [0] * ROWS
        col_has = [0] * COLS
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    row_has[i] += 1
                    col_has[j] += 1
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] != 1:
                    continue 
                else:
                    if row_has[i] > 1 or col_has[j] > 1:
                        res += 1
        return res                  
                