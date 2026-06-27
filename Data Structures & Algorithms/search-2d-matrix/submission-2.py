class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        return self.binarySearch(0, row * col - 1, matrix, target)

    def binarySearch(self, left: int, right: int, matrix: List[List[int]], target: int):
        if left > right:
            return False
        m = (left + right) // 2
        row, col = m // len(matrix[0]), m % len(matrix[0])
        
        val = matrix[row][col]
        if  val == target:
            return True
        elif val < target:
            return self.binarySearch(m + 1, right, matrix, target)
        else:
            return self.binarySearch(left, m - 1, matrix, target)
        


        