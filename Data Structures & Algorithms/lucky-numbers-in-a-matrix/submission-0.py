class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        
        rows_small = [0] * n
        cols_large = [0] * m

        for i in range(n):
            row_small = float('inf')
            for j in range(m):
                row_small = min(row_small, matrix[i][j])
            rows_small[i] = row_small
        
        for i in range(m):
            col_large = float('-inf')
            for j in range(n):
                col_large = max(col_large, matrix[j][i])
            cols_large[i] = col_large
        res = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == rows_small[i] == cols_large[j]:
                    res.append(matrix[i][j])
        return res 