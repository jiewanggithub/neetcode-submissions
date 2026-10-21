class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])

        for i in range(n):
            matrix[i].reverse()
        
        for i in range(n):
            for j in range(m - i - 1):
                matrix[i][j], matrix[n - j - 1][m - i - 1] = matrix[n - j - 1][m - i - 1],matrix[i][j] 
                

        


