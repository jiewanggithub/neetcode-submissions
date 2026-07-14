class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                adj[(x1, y1)].append((distance, x2, y2))
                adj[(x2, y2)].append((distance, x1, y1))
        
        visited = set()
        min_heap = [[0, points[0][0], points[0][1]]]
        res = 0

        while min_heap:
            w, x, y = heapq.heappop(min_heap)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            res += w

            for w, x, y in adj[(x, y)]:
                if (x, y) not in visited:
                    heapq.heappush(min_heap, [w, x, y])
        return res
