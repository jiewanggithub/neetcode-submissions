class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        visited = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == "0":
                return 
            
            if (i, j) in visited:
                return 
            
            grid[i][j] = 0
            visited.add((i, j))
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                dfs(nx, ny)
        
        res = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res 


        
