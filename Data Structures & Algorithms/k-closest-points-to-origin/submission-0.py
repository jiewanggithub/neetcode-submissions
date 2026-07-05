class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        for i, pair in enumerate(points):
            dis.append([math.sqrt((pair[0]**2 + pair[1]**2)), i])
        heapq.heapify(dis)

        res = []
        for _ in range(k):
            dist, i = heapq.heappop(dis)
            res.append(points[i])
        return res
        

