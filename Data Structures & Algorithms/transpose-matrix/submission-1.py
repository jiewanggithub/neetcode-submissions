class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # rotate 90 degree to the right
        # reverse each row 

        n, m = len(matrix), len(matrix[0])
        
        res = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                res[j][i] = matrix[i][j]

        for row in res:
            row = row[::-1]
        
        return res 