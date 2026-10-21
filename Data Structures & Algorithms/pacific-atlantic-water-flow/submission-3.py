class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(starts):
            visited = set(starts)
            stack = list(starts)

            while stack:
                i, j = stack.pop()

                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy

                    if (0 <= ni < n and
                        0 <= nj < m and
                        (ni, nj) not in visited and
                        heights[ni][nj] >= heights[i][j]):

                        visited.add((ni, nj))
                        stack.append((ni, nj))

            return visited

        # Pacific: top + left
        pacific = dfs(
            [(0, j) for j in range(m)] +
            [(i, 0) for i in range(n)]
        )

        # Atlantic: bottom + right
        atlantic = dfs(
            [(n - 1, j) for j in range(m)] +
            [(i, m - 1) for i in range(n)]
        )

        return [[i, j] for i, j in pacific & atlantic]

            