
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r, c = len(grid), len(grid[0])
        ans = [0] * len(queries)
        heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        point = 0

        for idx, q in sorted(enumerate(queries), key=lambda x: x[1]):
            while heap and heap[0][0] < q:
                val, i, j = heapq.heappop(heap)
                point += 1

                for dx, dy in dirs:
                    nx, ny = dx + i, dy + j
                    if not (0 <= nx < r and 0 <= ny < c):
                        continue 
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        heapq.heappush(heap, (grid[nx][ny], nx, ny))
            ans[idx] = point
        return ans 
                


        


            