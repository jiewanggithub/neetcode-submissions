class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        prefix_row1, prefix_row2 = grid[0].copy(), grid[1].copy()

        for i in range(1, N):
            prefix_row1[i] += prefix_row1[i - 1]
            prefix_row2[i] += prefix_row2[i - 1]

        res = float('inf') 
        for i in range(N):
            top = prefix_row1[-1] - prefix_row1[i]
            bottom = prefix_row2[i - 1] if i > 0 else 0
            robot2 = max(top, bottom)
            res = min(robot2, res)

        return res

