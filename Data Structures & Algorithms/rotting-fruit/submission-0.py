class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dire = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count_f = 0
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: 
                    count_f += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        time = 0
        while queue and count_f > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dire:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or 
                        nc >= COLS or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    count_f -= 1
                    queue.append((nr, nc))
            time += 1
        return time if count_f == 0 else -1 
