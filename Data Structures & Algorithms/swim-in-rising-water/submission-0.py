class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        pq = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        res = grid[0][0]
        while pq:
            time, r, c = heapq.heappop(pq)
            res = max(res, time)
            
            if (r, c) == (len(grid) - 1, len(grid) - 1):
                return res 

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    heapq.heappush(
                        pq,
                        (grid[nr][nc], nr, nc)
                    )
            
        return res
