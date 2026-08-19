class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        zero_row_set = set()
        zero_col_set = set()

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    zero_row_set.add(i)
                    zero_col_set.add(j)
                
        for i in range(ROWS):
            for j in range(COLS):
                if i in zero_row_set or j in zero_col_set:
                    matrix[i][j] = 0
        
        