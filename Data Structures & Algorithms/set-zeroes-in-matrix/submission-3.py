class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        first_row_zero = any(matrix[0][i] == 0 for i in range(COLS))
        first_col_zero = any(matrix[j][0] == 0 for j in range(ROWS))

        # Marking 
        for i in range(1, ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        # zero row 
        for i in range(1, ROWS):
            if matrix[i][0]== 0:
                for j in range(1, COLS):
                    matrix[i][j] = 0
        # zero col
        for i in range(COLS):
            if matrix[0][i] == 0:
                for j in range(1, ROWS):
                    matrix[j][i] = 0
        # zero first row 
        if first_row_zero:
            for i in range(COLS):
                matrix[0][i] = 0
        # zero first col
        if first_col_zero:
            for i in range(ROWS):
                matrix[i][0] = 0
        


        
        