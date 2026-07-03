"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        allSame = False
                        break

            if allSame:
                return Node(grid[r][c], 1)
            n //= 2
            topLeft = dfs(n, r, c)
            topRight = dfs(n, r, c+n)
            bottomLeft = dfs(n, n + r, c)
            bottomRight = dfs(n, n + r, n + c)
            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
        return dfs(len(grid), 0, 0)

