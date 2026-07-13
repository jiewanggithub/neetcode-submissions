class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        # (到达当前格子的最小 effort, row, col)
        pq = [(0, 0, 0)]
        visited = set()

        while pq:
            effort, r, c = heapq.heappop(pq)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            if r == ROWS - 1 and c == COLS - 1:
                return effort

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                    continue

                if (nr, nc) in visited:
                    continue

                diff = abs(heights[r][c] - heights[nr][nc])

                new_effort = max(effort, diff)

                heapq.heappush(
                    pq,
                    (new_effort, nr, nc)
                )

        return 0